# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from r_sam_roms import RSamRoms
from rom_info import RomInfo
from wiiflow_plugins_data import WiiFlowPluginsData


class RomImporter:
    def run(self):
        # 本函数用于导入 roms-import 文件夹里的 ROM 文件
        # 1. 新的 ROM 文件会被转移到 roms 文件夹，对应的 RomInfo 会
        #    记录在 roms-new.xml，需要进一步手动合入 roms.xml；
        # 2. 重复的 ROM 文件不会被转移，对应的 RomInfo 会记录在 roms-exist.xml
        wiiflow_plugins_data = WiiFlowPluginsData.instance()

        r_sam_roms = RSamRoms.instance()

        exist_rom_crc32_to_name = {}
        roms_new_xml_root = ET.Element("Game-List")

        import_dir_path = os.path.join(
            LocalConfigs.repository_directory(), "roms-import"
        )
        if not Helper.exist_directory(import_dir_path):
            print(f"【错误】无效的文件夹 {import_dir_path}")
            return

        roms_new_count = 0
        for src_rom_name in os.listdir(import_dir_path):
            if not ConsoleConfigs.rom_extension_match(src_rom_name):
                continue

            src_rom_path = os.path.join(import_dir_path, src_rom_name)
            src_rom_crc32 = Helper.compute_crc32(src_rom_path)
            if r_sam_roms.rom_exist(src_rom_crc32):
                exist_rom_crc32_to_name[src_rom_crc32] = src_rom_name
                continue

            src_rom_bytes = str(os.stat(src_rom_path).st_size)
            src_rom_title = Helper.get_rom_title(src_rom_name)

            game_info = wiiflow_plugins_data.query_game_info(
                rom_crc32=src_rom_crc32,
                rom_title=src_rom_title,
                en_title=src_rom_title,
                zhcn_title=src_rom_title,
            )
            if game_info is None:
                print(f'未知的游戏 crc32="{src_rom_crc32}" title="{src_rom_title}"')
                continue

            game_elem = ET.SubElement(
                roms_new_xml_root, "Game", {"name": game_info.name}
            )

            en_title = game_info.en_title
            zhcn_title = game_info.zhcn_title

            rom_info = RomInfo(
                game_name=game_info.name,
                rom_crc32=src_rom_crc32,
                rom_bytes=src_rom_bytes,
                rom_title=src_rom_title,
                en_title=en_title,
                zhcn_title=zhcn_title,
            )
            # 以 DB 中的命名为准
            rom_info.rom_title = game_info.rom_title
            r_sam_roms.add_rom_info(src_rom_crc32, rom_info)

            attribs = {
                "crc32": rom_info.rom_crc32,
                "bytes": rom_info.rom_bytes,
                "title": rom_info.rom_title,
                "en": rom_info.en_title,
                "zhcn": rom_info.zhcn_title,
                "apps-work": "",
                "apps-not-work": "",
            }
            ET.SubElement(game_elem, "Rom", attribs)

            print(f"新游戏入库 {src_rom_name}，crc32 = {src_rom_crc32}")
            if src_rom_title != game_info.rom_title:
                print(f"新游戏 {src_rom_name} 自动重命名为 {game_info.rom_title}")

            dst_rom_path = RSamRoms.compute_rom_path(rom_info)
            if os.path.exists(dst_rom_path):
                print(f"【错误】新游戏 {src_rom_name} 已经存在，但不在 .xml 文件中")
            elif Helper.verify_exist_directory_ex(os.path.dirname(dst_rom_path)):
                os.rename(src_rom_path, dst_rom_path)
            roms_new_count = roms_new_count + 1

        roms_exist_xml_path = os.path.join(
            LocalConfigs.repository_directory(), "roms\\roms-exist.xml"
        )
        if os.path.exists(roms_exist_xml_path):
            os.remove(roms_exist_xml_path)

        if len(exist_rom_crc32_to_name) > 0:
            roms_exist_xml_root = ET.Element("Game-List")
            for rom_crc32, rom_name in exist_rom_crc32_to_name.items():
                rom_info = r_sam_roms.query_rom_info(rom_crc32)
                game_elem = ET.SubElement(
                    roms_exist_xml_root, "Game", {"name": rom_info.game_name}
                )
                attribs = {
                    "crc32": rom_info.rom_crc32,
                    "bytes": rom_info.rom_bytes,
                    "rom": rom_info.rom_title,
                    "en": rom_info.en_title,
                    "zhcn": rom_info.zhcn_title,
                }
                ET.SubElement(game_elem, "Rom", attribs)
                print(f"{rom_name} 已经存在，官方名称为 {rom_info.rom_title}")

            ET.ElementTree(roms_exist_xml_root).write(
                roms_exist_xml_path, encoding="utf-8", xml_declaration=True
            )

        roms_new_xml_path = os.path.join(
            LocalConfigs.repository_directory(), "roms\\roms-new.xml"
        )
        if os.path.exists(roms_new_xml_path):
            os.remove(roms_new_xml_path)

        if roms_new_count == 0:
            print("没有新游戏")
        else:
            print(f"发现 {roms_new_count} 个新游戏")
            ET.ElementTree(roms_new_xml_root).write(
                roms_new_xml_path, encoding="utf-8", xml_declaration=True
            )


if __name__ == "__main__":
    RomImporter().run()
