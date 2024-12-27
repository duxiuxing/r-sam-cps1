# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.game_info import GameInfo
from common.helper import Helper
from common.local_configs import LocalConfigs

from ra_export_roms import RA_ExportFakeRoms
from wiiflow_plugins_data import WiiFlowPluginsData


class WiiFlow_ExportWfcCovers:
    def __init__(self):
        self.export_roms = None

    def run(self):
        if self.export_roms is None:
            print("WiiFlow_ExportWfcCovers 实例未指定 .export_roms")
            return

        wiiflow_plugins_data = WiiFlowPluginsData.instance()
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        dst_folder_path = os.path.join(
            LocalConfigs.export_root_folder_path(), f"wiiflow\\cache\\{plugin_name}"
        )
        if not Helper.verify_exist_folder_ex(dst_folder_path):
            print(f"【错误】无效的目标文件夹 {dst_folder_path}")
            return

        # 根据导出的 ROM 文件来拷贝对应的封面文件
        for rom_crc32, dst_rom_path in self.export_roms.rom_crc32_to_dst_path_items():
            game_info = wiiflow_plugins_data.query_game_info(rom_crc32=rom_crc32)
            if game_info is None:
                continue

            src_path = WiiFlowPluginsData.compute_wfc_cover_file_path(game_info)
            if not os.path.exists(src_path):
                print(f"【错误】无效的源文件 {src_path}")
                continue

            rom_name = os.path.basename(dst_rom_path)
            dst_path = os.path.join(dst_folder_path, f"{rom_name}.wfc")
            Helper.copy_file_if_not_exist(src_path, dst_path)


if __name__ == "__main__":
    export_roms = RA_ExportFakeRoms()
    export_roms.run()

    export_wfc_covers = WiiFlow_ExportWfcCovers()
    export_wfc_covers.export_roms = export_roms
    export_wfc_covers.run()
