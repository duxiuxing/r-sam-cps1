# -- coding: UTF-8 --

from console_configs import ConsoleConfigs
from ra_all_exporter import RA_AllExporter
from ra_configs import RA_Configs
from rom_export_configs import RomExportConfigs


class Menu_ExportRaFiles:
    @staticmethod
    def add_cmds(main_menu):
        rom_export_configs = RomExportConfigs()
        rom_export_configs.parse()

        ra_configs_file_name = "retroarch.xml"

        # export to Android in English
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_ANDROID)
        ra_configs.set_lang_code(RA_Configs.LANG_EN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        # main_menu.add_cmd(f"导出 {ra_configs.playlist_name()} 到 Android (英文)", ra_all_exporter)

        # export to Android in Simplified Chinese
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_ANDROID)
        ra_configs.set_lang_code(RA_Configs.LANG_ZHCN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        # main_menu.add_cmd(f"导出 {ra_configs.playlist_name()} 到 Android (简中)", ra_all_exporter)

        # export to Windows in English
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_WIN)
        ra_configs.set_lang_code(RA_Configs.LANG_EN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        main_menu.add_cmd(
            f"导出 {ra_configs.playlist_name()} 到 Windows (英文)", ra_all_exporter
        )

        # export to Windows in Simplified Chinese
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_WIN)
        ra_configs.set_lang_code(RA_Configs.LANG_ZHCN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        main_menu.add_cmd(
            f"导出 {ra_configs.playlist_name()} 到 Windows (简中)", ra_all_exporter
        )

        # export to XBOX in English
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_XBOX)
        ra_configs.set_lang_code(RA_Configs.LANG_EN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        # main_menu.add_cmd(f"导出 {ra_configs.playlist_name()} 到 XBOX (英文)", ra_all_exporter)

        # export to XBOX in Simplified Chinese
        ra_configs = RA_Configs(ra_configs_file_name)
        ra_configs.set_sys_code(RA_Configs.SYS_XBOX)
        ra_configs.set_lang_code(RA_Configs.LANG_ZHCN)
        ra_all_exporter = RA_AllExporter()
        ra_all_exporter.rom_export_configs = rom_export_configs
        ra_all_exporter.ra_configs = ra_configs
        # main_menu.add_cmd(f"导出 {ra_configs.playlist_name()} 到 XBOX (简中)", ra_all_exporter)
