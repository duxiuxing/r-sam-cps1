# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.game_info import GameInfo
from common.helper import Helper
from common.local_configs import LocalConfigs

from r_sam_roms import RSamRoms
from ra_export_roms import RA_ExportFakeRoms
from ra_export_thumbnails import RA_ExportThumbnails
from wiiflow_plugins_data import WiiFlowPluginsData


class WiiFlow_ExportSnapshots:
    def __init__(self):
        self.export_roms = None

    def run(self):
        if self.export_roms is None:
            print("WiiFlow_ExportSnapshots 实例未指定 .export_roms")
            return

        r_sam_roms = RSamRoms.instance()
        wiiflow_plugins_data = WiiFlowPluginsData.instance()
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        dst_folder_path = os.path.join(
            LocalConfigs.export_root_folder_path(), f"wiiflow\\snapshots\\{plugin_name}"
        )
        if not Helper.verify_exist_folder_ex(dst_folder_path):
            print(f"【错误】无效的目标文件夹 {dst_folder_path}")
            return

        # 根据导出的 ROM 文件来拷贝对应的封面文件
        for rom_crc32, dst_rom_path in self.export_roms.rom_crc32_to_dst_path_items():
            game_info = wiiflow_plugins_data.query_game_info(rom_crc32=rom_crc32)
            if game_info is None:
                continue

            # 优先使用 wiiflow\\snapshots 文件夹里的截图
            src_path = WiiFlowPluginsData.compute_snapshot_file_path(game_info)
            if not os.path.exists(src_path):
                # 使用 image\\snap 文件夹里的截图
                src_path = RSamRoms.compute_image_path(
                    r_sam_roms.query_rom_info(rom_crc32),
                    RA_ExportThumbnails.src_snap_folder(),
                )

            if not os.path.exists(src_path):
                print(f"【错误】无效的源文件 {src_path}")
                continue

            rom_name = os.path.basename(dst_rom_path)
            dst_path = os.path.join(
                dst_folder_path, f"{Helper.get_rom_title(rom_name)}.png"
            )
            Helper.copy_file_if_not_exist(src_path, dst_path)


if __name__ == "__main__":
    export_roms = RA_ExportFakeRoms()
    export_roms.run()

    export_snapshots = WiiFlow_ExportSnapshots()
    export_snapshots.export_roms = export_roms
    export_snapshots.run()
