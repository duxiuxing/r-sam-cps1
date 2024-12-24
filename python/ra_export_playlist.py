# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.label_value import EnLabelValue
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo
from common.path_value import WinPathValue


class RA_ExportPlaylist:
    def __init__(self):
        self.export_roms = None
        self.playlist_name = None
        self.playlist_label_value = EnLabelValue()
        self.playlist_path_value = WinPathValue()

    @staticmethod
    def __write_header(lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write('  "default_core_path": "",\n')
        lpl_file.write('  "default_core_name": "",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

    @staticmethod
    def __write_footer(lpl_file):
        lpl_file.write("\n  ]\n")
        lpl_file.write("}")

    @staticmethod
    def __export_assets_xmb_monochrome_png(playlist_name):
        src_playlist = os.path.join(
            LocalConfigs.repository_folder_path(),
            "image\\playlist\\playlist.png",
        )
        dst_playlist = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\assets\\xmb\\monochrome\\png\\{playlist_name}.png",
        )
        Helper.copy_file(src_playlist, dst_playlist)

        src_playlist_content = os.path.join(
            LocalConfigs.repository_folder_path(),
            "image\\playlist\\playlist-content.png",
        )
        dst_playlist_content = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\assets\\xmb\\monochrome\\png\\{playlist_name}-content.png",
        )
        Helper.copy_file(src_playlist_content, dst_playlist_content)

    def run(self):
        if self.export_roms is None:
            print("RA_ExportPlaylist 实例未指定 .export_roms")
            return

        if self.playlist_name is None:
            print("RA_ExportPlaylist 实例未指定 .playlist_name")
            return

        RA_ExportPlaylist.__export_assets_xmb_monochrome_png(self.playlist_name)

        xml_file_path = self.export_roms.config_file_path()
        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        lpl_file_path = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\playlists\\{self.playlist_name}.lpl",
        )
        if os.path.exists(lpl_file_path):
            os.remove(lpl_file_path)

        if not Helper.verify_folder_exist_ex(os.path.dirname(lpl_file_path)):
            return

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

            RA_ExportPlaylist.__write_header(lpl_file)

            first_rom = True

            for rom_elem in root.findall("Rom"):
                if first_rom:
                    first_rom = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                rom_crc32 = rom_elem.get("crc32").rjust(8, "0")

                value = self.playlist_path_value.parse(
                    self.export_roms.rom_dst_path(rom_crc32)
                )
                lpl_file.write(f'      "path": "{value}",\n')

                value = self.playlist_label_value.parse(rom_elem)
                lpl_file.write(f'      "label": "{value}",\n')

                lpl_file.write('      "core_path": "DETECT",\n')
                lpl_file.write('      "core_name": "DETECT",\n')
                lpl_file.write(f'      "crc32": "{rom_crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{self.playlist_name}.lpl"\n')
                lpl_file.write("    }")

            RA_ExportPlaylist.__write_footer(lpl_file)
            lpl_file.close()
