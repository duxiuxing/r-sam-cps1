# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase


class RA_ExportRoms(ExportRomsBase):
    @staticmethod
    def default_config_file_name():
        return "ra-roms.xml"

    @staticmethod
    def default_dst_folder_name():
        return ConsoleConfigs.ra_default_core_name()

    def __init__(self):
        super().__init__()
        self.config_file_name = RA_ExportRoms.default_config_file_name()
        self.dst_folder_name = RA_ExportRoms.default_dst_folder_name()
        self.export_fake_roms = False


class RA_ExportFakeRoms(ExportRomsBase):
    def __init__(self):
        super().__init__()
        self.config_file_name = RA_ExportRoms.default_config_file_name()
        self.dst_folder_name = RA_ExportRoms.default_dst_folder_name()
        self.export_fake_roms = True


if __name__ == "__main__":
    export_roms = RA_ExportFakeRoms()
    export_roms.run()
