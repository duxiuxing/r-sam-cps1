# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.label_value import EnLabelValue
from common.local_configs import LocalConfigs
from common.path_value import WiiSdPathValue

from ra_export_all import RA_ExportAll
from ra_export_roms import RA_ExportFakeRoms
from ra_export_roms import RA_ExportRoms
from wii_export_files import Wii_ExportFiles
from wiiflow_export_snapshots import WiiFlow_ExportSnapshots
from wiiflow_export_wfc_covers import WiiFlow_ExportWfcCovers


class Wii_ExportAll:
    @staticmethod
    def add_cmds(main_menu):
        wii_export_all = Wii_ExportAll()
        wii_export_all.export_roms = RA_ExportRoms()
        main_menu.add_cmd(
            f"导出 {ConsoleConfigs.ra_default_playlist_name_en()} 到 Wii SD",
            wii_export_all,
        )

    def __init__(self):
        self.export_roms = None

    def run(self):
        if self.export_roms is None:
            print("Wii_ExportAll 实例未指定 .export_roms")
            return False

        # export to Wii SD in English
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = ConsoleConfigs.ra_default_playlist_name_en()
        ra_export_all.export_roms = self.export_roms
        ra_export_all.playlist_label_value = EnLabelValue()
        ra_export_all.playlist_path_value = WiiSdPathValue()
        if ra_export_all.run() is False:
            return False

        export_files = Wii_ExportFiles()
        export_files.run()

        export_snapshots = WiiFlow_ExportSnapshots()
        export_snapshots.export_roms = self.export_roms
        export_snapshots.run()

        export_wfc_covers = WiiFlow_ExportWfcCovers()
        export_wfc_covers.export_roms = self.export_roms
        export_wfc_covers.run()
        return True


if __name__ == "__main__":
    export_all = Wii_ExportAll()
    export_all.export_roms = RA_ExportFakeRoms()
    export_all.run()
