# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo


class RSamRoms:
    __instance = None

    @staticmethod
    def instance():
        # 获取单例实例
        if RSamRoms.__instance is None:
            RSamRoms()
        return RSamRoms.__instance

    @staticmethod
    def compute_rom_path(rom_info):
        # 根据 rom_info 拼接 ROM 文件的路径
        if Helper.files_in_letter_folder():
            letter = rom_info.game_name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"roms\\{letter}\\{rom_info.game_name}\\{rom_info.rom_crc32}{ConsoleConfigs.rom_extension()}",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"roms\\{rom_info.game_name}\\{rom_info.rom_crc32}{ConsoleConfigs.rom_extension()}",
            )

    @staticmethod
    def compute_image_path(rom_info, sub_folder):
        # 根据 rom_info 和 sub_folder 拼接图片文件的路径
        if Helper.files_in_letter_folder():
            letter = rom_info.game_name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"image\\{sub_folder}\\{letter}\\{rom_info.game_name}.png",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"image\\{sub_folder}\\{rom_info.game_name}.png",
            )

    def __init__(self):
        if RSamRoms.__instance is not None:
            raise Exception("请使用 RSamRoms.instance() 获取实例")
        else:
            RSamRoms.__instance = self

        # rom_crc32 为键，RomInfo 为值的字典
        # 内容来自 roms 文件夹里的各个 .xml
        self.__rom_crc32_to_info = {}
        self.__load_rom_xml()

    def __load_xml_file(self, xml_file_path):
        if not os.path.exists(xml_file_path):
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        rom_extension = ConsoleConfigs.rom_extension()

        for game_elem in root.findall("Game"):
            game_name = game_elem.get("name")

            for rom_elem in game_elem.findall("Rom"):
                rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
                rom_info = RomInfo(
                    game_name=game_name,
                    rom_crc32=rom_crc32,
                    rom_bytes=rom_elem.get("bytes"),
                    rom_title=rom_elem.get("title"),
                    en_title=rom_elem.get("en"),
                    zhcn_title=rom_elem.get("zhcn"),
                )
                rom_path = RSamRoms.compute_rom_path(rom_info)
                if not os.path.exists(rom_path):
                    print(f"缺失 ROM 文件 {rom_path}")
                    continue
                else:
                    self.__rom_crc32_to_info[rom_crc32] = rom_info

    def __load_rom_xml(self):
        # 本函数执行的操作如下：
        # 1. 读取 roms 文件夹里的各个 .xml
        # 2. 设置 self.rom_crc32_to_info
        if Helper.files_in_letter_folder():
            for letter in "#ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                xml_file_path = os.path.join(
                    LocalConfigs.repository_folder_path(),
                    "roms\\{letter}\\{letter}.xml",
                )
                self.__load_xml_file(xml_file_path)
        else:
            xml_file_path = os.path.join(
                LocalConfigs.repository_folder_path(), "roms\\roms.xml"
            )
            self.__load_xml_file(xml_file_path)

    def rom_crc32_to_info_items(self):
        return self.__rom_crc32_to_info.items()

    def rom_exist(self, rom_crc32):
        return rom_crc32 in self.__rom_crc32_to_info.keys()

    def query_rom_info(self, rom_crc32):
        if self.rom_exist(rom_crc32):
            return self.__rom_crc32_to_info[rom_crc32]
        else:
            return None

    def add_rom_info(self, rom_crc32, rom_info):
        self.__rom_crc32_to_info[rom_crc32] = rom_info


if __name__ == "__main__":
    r_sam_roms = RSamRoms()
    r_sam_roms.query_rom_info("00000000")
