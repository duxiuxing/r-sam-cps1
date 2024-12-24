# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from configparser import ConfigParser

from common.console_configs import ConsoleConfigs
from common.game_info import GameInfo
from common.helper import Helper
from common.local_configs import LocalConfigs


class WiiFlowPluginsData:
    __instance = None

    @staticmethod
    def instance():
        # 获取单例实例
        if WiiFlowPluginsData.__instance is None:
            WiiFlowPluginsData()
        return WiiFlowPluginsData.__instance

    @staticmethod
    def ini_file_path():
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()
        return os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wiiflow\\plugins_data\\{plugin_name}\\{plugin_name}.ini",
        )

    @staticmethod
    def xml_file_path():
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()
        return os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wiiflow\\plugins_data\\{plugin_name}\\{plugin_name}.xml",
        )

    @staticmethod
    def compute_png_cover_file_path(game_info):
        # 根据 game_info 拼接 .png 格式的封面文件路径
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        if Helper.files_in_letter_folder():
            letter = game_info.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\boxcovers\\\{plugin_name}\\{letter}\\{game_info.rom_title}{ConsoleConfigs.rom_extension()}.png",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\boxcovers\\\{plugin_name}\\{game_info.rom_title}{ConsoleConfigs.rom_extension()}.png",
            )

    @staticmethod
    def compute_wfc_cover_file_path(game_info):
        # 根据 game_info 拼接 .wfc 格式的封面文件路径
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        if Helper.files_in_letter_folder():
            letter = game_info.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\cache\\\{plugin_name}\\{letter}\\{game_info.rom_title}{ConsoleConfigs.rom_extension()}.wfc",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\cache\\\{plugin_name}\\{game_info.rom_title}{ConsoleConfigs.rom_extension()}.wfc",
            )

    @staticmethod
    def compute_snapshot_file_path(game_info):
        # 根据 game_info 拼接游戏截图文件路径
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        if Helper.files_in_letter_folder():
            letter = game_info.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\snapshots\\\{plugin_name}\\{letter}\\{game_info.rom_title}.png",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"wii\\wiiflow\\snapshots\\\{plugin_name}\\{game_info.rom_title}.png",
            )

    def __init__(self):
        if WiiFlowPluginsData.__instance is not None:
            raise Exception("请使用 WiiFlowPluginsData.instance() 获取实例")
        else:
            WiiFlowPluginsData.__instance = self

        # game_id 为键，GameInfo 为值的字典
        # 内容来自 WiiFlowPluginsData.xml_file_path()
        self.game_id_to_info = {}
        self.__load_xml_file()

        # rom_crc32 为键，game_id 为值的字典
        # 内容来自 WiiFlowPluginsData.ini_file_path()
        self.rom_crc32_to_game_id = {}

        # rom_title 为键，game_id 为值的字典
        # 内容来自 WiiFlowPluginsData.ini_file_path()
        self.rom_title_to_game_id = {}
        self.__load_ini_file()

    def __load_xml_file(self):
        # 本函数执行的操作如下：
        # 1. 读取 WiiFlowPluginsData.xml_file_path()
        # 2. 设置 self.game_id_to_info

        xml_file_path = WiiFlowPluginsData.xml_file_path()

        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        self.game_id_to_info.clear()
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for game_elem in root.findall("game"):
            game_name = game_elem.get("name")
            game_id = ""
            en_title = ""
            zhcn_title = ""
            for elem in game_elem:
                if elem.tag == "id":
                    game_id = elem.text
                elif elem.tag == "locale":
                    lang = elem.get("lang")
                    if lang == "EN":
                        en_title = elem.find("title").text
                        if en_title not in game_name.split(" / "):
                            print("英文名不一致")
                            print(f"\tname     = {game_name}")
                            print(f"\tEN title = {en_title}")
                    elif lang == "ZHCN":
                        zhcn_title = elem.find("title").text

            self.game_id_to_info[game_id] = GameInfo(
                id=game_id, name=game_name, en_title=en_title, zhcn_title=zhcn_title
            )

    def __load_ini_file(self):
        # 本函数执行的操作如下：
        # 1. 读取 WiiFlowPluginsData.ini_file_path()
        # 2. 设置 self.rom_crc32_to_game_id 和 self.rom_title_to_game_id
        # 3. 设置 self.game_id_to_info 每个 GameInfo 的 rom_title
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()
        ini_file_path = WiiFlowPluginsData.ini_file_path()

        if not os.path.exists(ini_file_path):
            print(f"无效的文件：{ini_file_path}")
            return

        self.rom_crc32_to_game_id.clear()
        self.rom_title_to_game_id.clear()

        ini_parser = ConfigParser()
        ini_parser.read(ini_file_path)
        if ini_parser.has_section(plugin_name):
            for rom_title in ini_parser[plugin_name]:
                values = ini_parser[plugin_name][rom_title].split("|")
                game_id = values[0]
                self.rom_title_to_game_id[rom_title] = game_id

                rom_crc32_list = set()
                for index in range(1, len(values) - 1):
                    rom_crc32 = values[index].rjust(8, "0")
                    rom_crc32_list.add(rom_crc32)
                    self.rom_crc32_to_game_id[rom_crc32] = game_id

                if game_id in self.game_id_to_info.keys():
                    self.game_id_to_info[game_id].rom_title = rom_title
                    self.game_id_to_info[game_id].rom_crc32_list = rom_crc32_list
                else:
                    print(f"{plugin_name}.xml 中未发现 game_id = {game_id}")

    def query_game_info(
        self, rom_crc32=None, rom_title=None, en_title=None, zhcn_title=None
    ):
        # 根据 rom_crc32 或 rom_title 查询游戏信息
        # Args:
        #     rom_crc32 (str): ROM 文件的 CRC32，查找优先级高
        #     rom_title (str): ROM 文件的标题，比如 1941.zip 的标题就是 1941，查找优先级低
        # Returns:
        #     找到则返回 GameInfo 对象，仅以下字段有效：
        #         - GameInfo.rom_title  : ROM 文件的标题，如 1941.zip 的标题就是 1941
        #         - GameInfo.en_title   : 游戏的英文名
        #         - GameInfo.zhcn_title : 游戏的中文名
        #
        #     没找到则返回 None
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        game_id = None
        if rom_crc32 is not None:
            if rom_crc32 in self.rom_crc32_to_game_id.keys():
                game_id = self.rom_crc32_to_game_id.get(rom_crc32)
            else:
                print(f"{plugin_name}.ini 中未发现 rom_crc32 = {rom_crc32}")

        if game_id is None and rom_title is not None:
            if rom_title in self.rom_title_to_game_id.keys():
                game_id = self.rom_title_to_game_id.get(rom_title)
            else:
                print(f"{plugin_name}.ini 中未发现 rom_title = {rom_title}")

        if game_id is not None and game_id in self.game_id_to_info.keys():
            return self.game_id_to_info.get(game_id)

        if en_title is None and zhcn_title is None:
            return None

        en_title_without_region = en_title
        if en_title is not None:
            en_title_without_region = Helper.remove_region(en_title)

        zhcn_title_without_region = zhcn_title
        if zhcn_title is not None:
            zhcn_title_without_region = Helper.remove_region(zhcn_title)

        for game_info in self.game_id_to_info.values():
            if en_title is not None:
                if (
                    game_info.en_title == en_title
                    or game_info.en_title == en_title_without_region
                ):
                    return game_info
            if zhcn_title is not None:
                if (
                    game_info.zhcn_title == zhcn_title
                    or game_info.zhcn_title == zhcn_title_without_region
                ):
                    return game_info

        print(f"{plugin_name}.xml 中未发现 rom_title = {rom_title}")
        return None

    def export_all_fake_roms_to(self, dst_folder_path):
        # 防止重复读取
        if len(self.game_id_to_info) == 0:
            self.reset()

        for game_info in self.game_id_to_info.values():
            dst_path = os.path.join(
                dst_folder_path,
                f"{game_info.rom_title}{ConsoleConfigs.rom_extension()}",
            )
            if not os.path.exists(dst_path):
                open(dst_path, "w").close()


if __name__ == "__main__":
    plugins_data = WiiFlowPluginsData()
    dst_folder_path = os.path.join(
        LocalConfigs.export_root_folder_path(),
        f"roms\\{ConsoleConfigs.short_name()}",
    )
    Helper.verify_folder_exist_ex(dst_folder_path)
    plugins_data.export_all_fake_roms_to(dst_folder_path)
