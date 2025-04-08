# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath
from rom_export_configs import RomExportConfigs
from rom_exporter import RomExporter
from wii_app_icon_exporter import Wii_AppIconExporter
from wii_ra_ss_cfg_exporter import WiiRA_SS_CfgExporter
from wii_ra_app_configs import WiiRA_AppConfigs
from wiiflow_plugins_data import WiiFlowPluginsData


class WiiRA_SS_AppExporter:
    def __init__(self):
        self.rom_export_configs = None
        self.app_configs = None

    def _copy_ra_ss_core_file(self):
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        ra_configs = ConsoleConfigs.ra_configs()
        src_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\apps\\RA-HEXAECO\\{ra_configs.ra_ss_core_file()}",
        )
        dst_file_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\boot.dol",
        )
        Helper.copy_file(src_file_path, dst_file_path)

    def _copy_ra_ss_data_folder(self):
        ra_configs = ConsoleConfigs.ra_configs()
        src_root = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\private\\{ra_configs.ra_ss_data_folder()}",
        )
        dst_root = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"private\\{ra_configs.ra_ss_data_folder()}",
        )

        folder_list = ["audiofilters", "overlays", "videofilters"]
        for folder in folder_list:
            src_dir = os.path.join(src_root, folder)
            dst_dir = os.path.join(dst_root, folder)
            Helper.copy_directory(src_dir, dst_dir)

    def _export_meta_xml(self):
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        src_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\apps\\{app_configs.folder}\\meta-{ConsoleConfigs.storage_device_code()}.xml",
        )
        dst_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\meta.xml",
        )
        if os.path.exists(dst_path):
            os.remove(dst_path)
        if os.path.exists(src_path):
            Helper.copy_file(src_path, dst_path)
            return

        if Helper.verify_exist_directory_ex(os.path.dirname(dst_path)) is False:
            print(f"【警告】无效的目标文件 {dst_path}")
            return

        game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=app_configs.rom_title
        )
        with open(dst_path, "w", encoding="utf-8") as xml_file:
            ra_configs = ConsoleConfigs.ra_configs()

            xml_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            xml_file.write('<app version="1">\n')
            xml_file.write(f"  <name>{app_configs.name}</name>\n")
            xml_file.write("  <author>RunningSnakes &amp; R-Sam</author>\n")
            xml_file.write(
                f"  <version>{ConsoleConfigs.storage_device_code().upper()}</version>\n"
            )
            xml_file.write("  <release_date>2024/08/15</release_date>\n")
            xml_file.write(
                f"  <short_description>{ra_configs.short_description()}</short_description>\n"
            )
            xml_file.write(f"  <long_description>{game_info.name}\n")

            if game_info.developer == game_info.publisher:
                xml_file.write(f"- Developer &amp; Publisher : {game_info.developer}\n")
            else:
                xml_file.write(f"- Developer : {game_info.developer}\n")
                xml_file.write(f"- Publisher : {game_info.publisher}\n")

            xml_file.write(f"- Genre : {game_info.genre}\n")
            xml_file.write(f"- Release Date : {game_info.date}\n")
            xml_file.write(f"- Max Players : {game_info.players}\n\n")

            xml_file.write(
                f"Wii Channel : {ConsoleConfigs.storage_device_code()}:/wad/{app_configs.name}\n"
            )
            xml_file.write(f"Website : {ConsoleConfigs.website()}</long_description>\n")
            xml_file.write("  <no_ios_reload/>\n")
            xml_file.write("  <ahb_access/>\n")
            xml_file.write("  <arguments>\n")

            rom_export_info = self.rom_export_configs.rom_export_info_list()[0]
            dir_path = Wii_PlaylistPath().parse(
                os.path.dirname(rom_export_info.dst_path)
            )
            xml_file.write(f"    <arg>{dir_path}</arg>\n")

            file_name = os.path.basename(rom_export_info.dst_path)
            xml_file.write(f"    <arg>{file_name}</arg>\n")

            cfg_path = os.path.join(
                LocalConfigs.root_directory_export_to(),
                f"private\\{ra_configs.ra_ss_data_folder()}\\{app_configs.rom_title}.cfg",
            )
            cfg_path = Wii_PlaylistPath().parse(cfg_path)
            xml_file.write(f"    <arg>{cfg_path}</arg>\n")

            xml_file.write("  </arguments>\n</app>\n")
            xml_file.close()

    def run(self):
        if self.rom_export_configs is None:
            print("【错误】未指定 rom_export_configs: RomExportConfigs")
            return

        ra_configs = ConsoleConfigs.ra_configs()

        if ra_configs.sys_code() != RA_Configs.SYS_WII:
            print(
                f"【错误】sys_code 当前值={ra_configs.sys_code()}，预期值={RA_Configs.SYS_WII}"
            )
            return

        if ra_configs.lang_code() != RA_Configs.LANG_EN:
            print(
                f"lang_code 当前值={ra_configs.lang_code()}，预期值={RA_Configs.LANG_EN}"
            )
            return

        if self.app_configs is None:
            print("【错误】未指定 app_configs: Wii_RaAppConfigs")
            return
        old_app_configs = ConsoleConfigs.set_wii_ra_app_configs(self.app_configs)

        old_rom_filter = self.rom_export_configs.rom_title_filter
        self.rom_export_configs.rom_title_filter = self.app_configs.rom_title

        RomExporter(self.rom_export_configs).run()

        self._copy_ra_ss_core_file()
        self._copy_ra_ss_data_folder()
        Wii_AppIconExporter().run()
        self._export_meta_xml()
        WiiRA_SS_CfgExporter(self.app_configs.rom_title, self.app_configs.remap).run()

        ConsoleConfigs.set_wii_ra_app_configs(old_app_configs)
        self.rom_export_configs.rom_title_filter = old_rom_filter
