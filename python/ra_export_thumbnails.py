# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.label_value import EnLabelValue
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo

from r_sam_roms import RSamRoms


class RA_ExportThumbnails:
    @staticmethod
    def default_src_boxart_folder():
        return "boxart"

    @staticmethod
    def src_snap_folder():
        return "snap"

    @staticmethod
    def src_title_folder():
        return "title"

    def __init__(self):
        self.export_roms = None
        self.playlist_name = None
        self.playlist_label_value = EnLabelValue()
        self.src_boxart_folder = RA_ExportThumbnails.default_src_boxart_folder()

    def run(self):
        if self.export_roms is None:
            print("RA_ExportThumbnails 实例未指定 .export_roms")
            return

        if self.playlist_name is None:
            print("RA_ExportThumbnails 实例未指定 .playlist_name")
            return

        r_sam_roms = RSamRoms.instance()

        xml_file_path = self.export_roms.config_file_path()
        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for rom_elem in root.findall("Rom"):
            rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
            rom_info = r_sam_roms.query_rom_info(rom_crc32)

            image_name = self.playlist_label_value.parse(rom_elem)

            src_boxart_path = RSamRoms.compute_image_path(
                rom_info, self.src_boxart_folder
            )
            dst_boxart_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.playlist_name}\\Named_Boxarts\\{image_name}.png",
            )
            Helper.copy_file(src_boxart_path, dst_boxart_path)

            src_snap_path = RSamRoms.compute_image_path(
                rom_info, RA_ExportThumbnails.src_snap_folder()
            )
            dst_snap_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.playlist_name}\\Named_Snaps\\{image_name}.png",
            )
            Helper.copy_file(src_snap_path, dst_snap_path)

            src_title_path = RSamRoms.compute_image_path(
                rom_info, RA_ExportThumbnails.src_title_folder()
            )
            dst_title_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.playlist_name}\\Named_Titles\\{image_name}.png",
            )
            Helper.copy_file(src_title_path, dst_title_path)
