# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from rom_export_configs import RomExportConfigs
from rom_export_info import RomExportInfo


class RomExporter:
    def __init__(self, configs: RomExportConfigs):
        self.configs = configs

    def run(self):
        if not Helper.verify_exist_directory_ex(self.configs.dst_roms_directory):
            print(f"【错误】无效的目标文件夹 {self.configs.dst_roms_directory}")
            return False

        bios_file = ConsoleConfigs.bios_file()
        for item in self.configs.rom_export_info_list():
            src_path = item.src_path
            dst_path = item.dst_path
            if Helper.verify_exist_directory_ex(os.path.dirname(dst_path)):
                if self.configs.export_fake_rom:
                    if not os.path.exists(dst_path):
                        open(dst_path, "w").close()
                else:
                    Helper.copy_file_if_not_exist(src_path, dst_path)

            if bios_file is not None:
                src_bios_path = os.path.join(
                    LocalConfigs.repository_directory(), f"roms\\{bios_file}"
                )
                dst_bios_path = os.path.join(os.path.dirname(dst_path), bios_file)
                Helper.copy_file_if_not_exist(src_bios_path, dst_bios_path)

        if self.configs.export_fake_rom:
            print(f"导出空的 ROM 文件到 {self.configs.dst_roms_directory}")
        else:
            print(f"导出 ROM 文件到 {self.configs.dst_roms_directory}")

        return True


if __name__ == "__main__":
    rom_export_configs = RomExportConfigs()
    rom_export_configs.export_fake_rom = True
    rom_export_configs.parse()

    RomExporter(rom_export_configs).run()
