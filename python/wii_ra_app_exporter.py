# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from ra_all_exporter import RA_AllExporter
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath
from rom_export_configs import RomExportConfigs
from wii_app_icon_exporter import Wii_AppIconExporter
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_cfg_exporter import WiiRA_CfgExporter
from wiiflow_plugins_data import WiiFlowPluginsData


class WiiRA_AppExporter:
    def __init__(self):
        self.rom_export_configs = None
        self.app_configs = None

    def _copy_ra_core_files(self):
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        src_dir_path = os.path.join(
            LocalConfigs.repository_directory(), "wii\\apps\\retroarch-wii\\info"
        )
        dst_dir_path = os.path.join(
            LocalConfigs.root_directory_export_to(), f"apps\\{app_configs.folder}\\info"
        )
        Helper.copy_directory(src_dir_path, dst_dir_path)

        ra_configs = ConsoleConfigs.ra_configs()
        src_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\apps\\retroarch-wii\\{ra_configs.core_file()}",
        )
        dst_file_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\{ra_configs.core_file()}",
        )
        Helper.copy_file(src_file_path, dst_file_path)

        dst_file_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\boot.dol",
        )
        Helper.copy_file(src_file_path, dst_file_path)

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
            xml_file.write("  <author>Libretro Team &amp; R-Sam</author>\n")
            xml_file.write(
                f"  <version>{ra_configs.version()} {ConsoleConfigs.storage_device_code().upper()}</version>\n"
            )
            xml_file.write(
                f"  <release_date>{ra_configs.release_date()}</release_date>\n"
            )
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
            xml_file.write(
                "Website : https://github.com/R-Sam-1980/cps3</long_description>\n"
            )
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

        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = self.rom_export_configs
        ra_all_exporter.run()

        self._copy_ra_core_files()
        Wii_AppIconExporter().run()
        self._export_meta_xml()
        WiiRA_CfgExporter().run()

        ConsoleConfigs.set_wii_ra_app_configs(old_app_configs)
        self.rom_export_configs.rom_title_filter = old_rom_filter
