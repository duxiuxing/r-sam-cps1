# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from r_sam_roms import RSamRoms
from wii_ra_app_configs import WiiRA_AppConfigs
from wiiflow_plugins_data import WiiFlowPluginsData


class Wii_AppIconExporter:
    def run(self):
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        src_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\apps\\{app_configs.folder}\\icon.png",
        )
        dst_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\icon.png",
        )
        if os.path.exists(dst_path):
            os.remove(dst_path)
        if os.path.exists(src_path):
            Helper.copy_file(src_path, dst_path)
            return

        game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=app_configs.rom_title
        )
        logo_path = RSamRoms.compute_image_path(game_info.name, "logo")
        Image.open(logo_path).resize((128, 48)).save(dst_path)
