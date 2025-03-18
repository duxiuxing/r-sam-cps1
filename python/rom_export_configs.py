# -- coding: UTF-8 --

import os
import random
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from local_configs import LocalConfigs
from r_sam_roms import RSamRoms
from rom_export_info import RomExportInfo
from rom_info import RomInfo


class RomExportConfigs:
    def __init__(self):
        self.rom_title_filter = None
        self.export_fake_rom = False
        self.all_rom_export_info_list = []
        self.dst_roms_directory = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"Games\\{ConsoleConfigs.ra_configs().core_name()}",
        )

    def rom_export_info_list(self):
        ret_list = []
        if self.rom_title_filter is None:
            ret_list.extend(self.all_rom_export_info_list)
        else:
            for rom_export_info in self.all_rom_export_info_list:
                if rom_export_info.rom_title == self.rom_title_filter:
                    ret_list.append(rom_export_info)
                    break
        return ret_list

    def parse(self, xml_file_name="rom-export.xml"):
        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"config\\{xml_file_name}",
        )
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效的文件 {xml_file_path}")
            return False

        self.all_rom_export_info_list = []
        r_sam_roms = RSamRoms.instance()

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        if "dst_folder" in root.attrib:
            self.dst_roms_directory = os.path.join(
                LocalConfigs.root_directory_export_to(), root.get("dst_folder")
            )

        one_folder_one_rom = False
        if (
            "one_folder_one_rom" in root.attrib
            and root.get("one_folder_one_rom").lower() == "true"
        ):
            one_folder_one_rom = True

        for rom_elem in root:
            rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
            rom_info = r_sam_roms.query_rom_info(rom_crc32)
            if rom_info is None:
                print(f'crc32="{rom_crc32}" 的 ROM 文件不存在')
                continue

            rom_bytes = rom_elem.get("bytes")
            if rom_bytes != rom_info.rom_bytes:
                print(
                    f'crc32="{rom_crc32}" 的 ROM 文件存在错误的属性：bytes="{rom_bytes}"'
                )
                continue

            rom_title = rom_elem.get("title")
            if rom_title != rom_info.rom_title:
                print(
                    f'crc32="{rom_crc32}" 的 ROM 文件存在错误的属性：title="{rom_title}"'
                )
                continue

            src_path = RSamRoms.compute_rom_path(rom_info)
            if not os.path.exists(src_path):
                print(f"【错误】无效的源文件 {src_path}")
                continue

            rom_export_info = RomExportInfo(rom_info)
            rom_export_info.src_path = src_path

            if "en" in rom_elem.attrib:
                rom_export_info.en_title = rom_elem.get("en")
            if "zhcn" in rom_elem.attrib:
                rom_export_info.zhcn_title = rom_elem.get("zhcn")

            rom_name = rom_title + ConsoleConfigs.rom_extension()
            if one_folder_one_rom:
                # 把 ROM 文件放在以游戏命名的文件夹里
                rom_name = f"{rom_info.game_name}\\{rom_name}"
            rom_export_info.dst_path = os.path.join(self.dst_roms_directory, rom_name)

            self.all_rom_export_info_list.append(rom_export_info)

        return True


if __name__ == "__main__":
    rom_export_configs = RomExportConfigs()
    rom_export_configs.parse()
    print("Index\t | ROM\t\t\t | Game")
    index = 1
    for rom_export_info in rom_export_configs.rom_export_info_list():
        print(
            f"{index}.\t | {rom_export_info.rom_title}{ConsoleConfigs.rom_extension()}\t\t | {rom_export_info.game_name}"
        )
        index = index + 1

    random_index = random.randrange(0, index)
    rom_export_info = rom_export_configs.rom_export_info_list()[random_index]
    rom_export_configs.rom_title_filter = rom_export_info.rom_title
    print(f"\nSet {rom_export_info.rom_title} as filter")
    print("Index\t | ROM\t\t\t | Game")
    index = 1
    for rom_export_info in rom_export_configs.rom_export_info_list():
        print(
            f"{index}.\t | {rom_export_info.rom_title}{ConsoleConfigs.rom_extension()}\t\t | {rom_export_info.game_name}"
        )
        index = index + 1
