# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from common.label_value import EnLabelValue, ZhcnLabelValue
from common.path_value import AndroidPathValue, WinPathValue, XBoxPathValue

from ra_export_all import RA_ExportAll
from ra_export_roms import RA_ExportRoms


class RA_ExportMenu:
    @staticmethod
    def add_cmds(main_menu):
        export_roms = RA_ExportRoms()
        playlist_name_en = ConsoleConfigs.ra_default_playlist_name_en()
        playlist_name_zhcn = ConsoleConfigs.ra_default_playlist_name_zhcn()

        # export to Android in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = AndroidPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Android (英文)", export_all)

        # export to Android in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = AndroidPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Android (简中)", export_all)

        # export to Windows in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = WinPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Windows (英文)", export_all)

        # export to Windows in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = WinPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Windows (简中)", export_all)

        # export to XBOX in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = XBoxPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 XBOX (英文)", export_all)

        # export to XBOX in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = XBoxPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 XBOX (简中)", export_all)
