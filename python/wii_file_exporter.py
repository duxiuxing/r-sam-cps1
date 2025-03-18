# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from ra_configs import RA_Configs
from rom_export_configs import RomExportConfigs
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app_exporter import WiiRA_AppExporter
from wii_ra_ss_app_exporter import WiiRA_SS_AppExporter


class WiiFileExporter:
    WiiRA_App = "WiiRA_App"
    WiiRA_SS_App = "WiiRA_SS_App"

    def __init__(self, app_name_filter=None, app_type_filter=None):
        self._app_name_filter = app_name_filter
        self._app_type_filter = app_type_filter
        self._rom_export_configs = None

    @staticmethod
    def export_files_and_folders(app_elem):
        src_root = LocalConfigs.repository_directory()
        dst_root = LocalConfigs.root_directory_export_to()

        for elem in app_elem.findall("Folder"):
            src_path = os.path.join(src_root, elem.get("src"))
            dst_path = os.path.join(dst_root, elem.get("dst"))
            Helper.copy_directory(src_path, dst_path)

        for elem in app_elem.findall("File"):
            src_path = os.path.join(src_root, elem.get("src"))
            dst_path = os.path.join(dst_root, elem.get("dst"))
            Helper.copy_file(src_path, dst_path)

    def export_wii_ra_app(self, app_elem):
        if (
            self._app_name_filter is not None
            and app_elem.get("name") != self._app_name_filter
        ):
            return

        app_exporter = WiiRA_AppExporter()
        app_exporter.rom_export_configs = self._rom_export_configs

        app_configs = WiiRA_AppConfigs()
        app_configs.name = app_elem.get("name")
        app_configs.folder = app_elem.get("folder")
        if "rom_title" in app_elem.attrib:
            app_configs.rom_title = app_elem.get("rom_title")
        if (
            "content_show_favorites" in app_elem.attrib
            and app_elem.get("content_show_favorites").lower() == "true"
        ):
            app_configs.content_show_favorites = True
        if (
            "content_show_history" in app_elem.attrib
            and app_elem.get("content_show_history").lower() == "true"
        ):
            app_configs.content_show_history = True
        if "remap" in app_elem.attrib:
            app_configs.remap = app_elem.get("remap")
        app_exporter.app_configs = app_configs
        app_exporter.run()
        WiiFileExporter.export_files_and_folders(app_elem)

    def export_wii_ra_ss_app(self, app_elem):
        if (
            self._app_name_filter is not None
            and app_elem.get("name") != self._app_name_filter
        ):
            return

        app_exporter = WiiRA_SS_AppExporter()
        app_exporter.rom_export_configs = self._rom_export_configs

        app_configs = WiiRA_AppConfigs()
        app_configs.name = app_elem.get("name")
        app_configs.folder = app_elem.get("folder")
        if "rom_title" in app_elem.attrib:
            app_configs.rom_title = app_elem.get("rom_title")
        if "remap" in app_elem.attrib:
            app_configs.remap = app_elem.get("remap")
        app_exporter.app_configs = app_configs
        app_exporter.run()
        WiiFileExporter.export_files_and_folders(app_elem)

    def run(self):
        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            "config\\wii-file-export.xml",
        )

        if not os.path.exists(xml_file_path):
            print(f"【警告】无效的文件 {xml_file_path}")
            return

        self._rom_export_configs = RomExportConfigs()
        self._rom_export_configs.parse()

        old_ra_configs = ConsoleConfigs.ra_configs()

        ra_configs = RA_Configs("retroarch.xml")
        ra_configs.set_sys_code(RA_Configs.SYS_WII)
        ra_configs.set_lang_code(RA_Configs.LANG_EN)
        old_ra_configs = ConsoleConfigs.set_ra_configs(ra_configs)

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for elem in root:
            if elem.tag == WiiFileExporter.WiiRA_App:
                if (
                    self._app_type_filter is not None
                    and self._app_type_filter != WiiFileExporter.WiiRA_App
                ):
                    continue
                self.export_wii_ra_app(elem)
            elif elem.tag == WiiFileExporter.WiiRA_SS_App:
                if (
                    self._app_type_filter is not None
                    and self._app_type_filter != WiiFileExporter.WiiRA_SS_App
                ):
                    continue
                self.export_wii_ra_ss_app(elem)

        ConsoleConfigs.set_ra_configs(old_ra_configs)
