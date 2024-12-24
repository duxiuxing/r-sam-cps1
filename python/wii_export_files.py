# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_files_base import ExportFilesBase


class Wii_ExportFiles(ExportFilesBase):
    @staticmethod
    def default_config_file_name():
        return "wii-files.xml"

    def __init__(self):
        super().__init__()
        self.config_file_name = Wii_ExportFiles.default_config_file_name()


if __name__ == "__main__":
    export_files = Wii_ExportFiles()
    export_files.run()
