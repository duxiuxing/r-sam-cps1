# -- coding: UTF-8 --

import os

from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class S_BannerInfo:
    CAPCOM_LOGO_WIDTH = 142
    CAPCOM_LOGO_HEIGHT = 29
    CAPCOM_LOGO_OFFSET_X_TOP = 34
    CAPCOM_LOGO_OFFSET_X_BOTTOM = 6
    CAPCOM_LOGO_OFFSET_Y = 8
    CAPCOM_LOGO_ALIGN_LEFT_TOP = (34, 8)
    CAPCOM_LOGO_ALIGN_LEFT_BOTTOM = (6, 297)
    CAPCOM_LOGO_ALIGN_RIGHT_TOP = (414, 8)  # 414=590-142-34
    CAPCOM_LOGO_ALIGN_RIGHT_BOTTOM = (442, 297)  # 442=590-142-6

    MENU_SCREEN_WIDTH = 590
    MENU_SCREEN_HEIGHT = 332

    def __init__(
        self, rom_title, game_logo_size, game_logo_left_top, capcom_logo_left_top
    ):
        self.rom_title = rom_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.capcom_logo_left_top = capcom_logo_left_top


class Wii_MakeStandardBanner:
    def __init__(self, banner_info):
        self.banner_info = banner_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=banner_info.rom_title
        )

    def make_main_screen_bg(self):
        main_screen_bg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\standard\\MenuScreen1-bg.png",
        )
        if os.path.exists(main_screen_bg_path):
            return Image.open(main_screen_bg_path)
        else:
            wallpaper_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\wallpaper\\{self.game_info.name}.jpg",
            )
            image = Image.open(wallpaper_path).resize(
                (S_BannerInfo.MENU_SCREEN_WIDTH, S_BannerInfo.MENU_SCREEN_HEIGHT)
            )
            Helper.verify_exist_directory_ex(os.path.dirname(main_screen_bg_path))
            image.save(main_screen_bg_path, format="PNG")
            return image

    def run(self):
        main_screen_bg = self.make_main_screen_bg()

        if self.banner_info.game_logo_size != (0, 0):
            game_logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\standard\\logo.png",
            )
            if not os.path.exists(game_logo_path):
                game_logo_path = os.path.join(
                    LocalConfigs.repository_directory(),
                    f"image\\logo\\{self.game_info.name}.png",
                )
            game_logo = Image.open(game_logo_path).resize(
                self.banner_info.game_logo_size
            )
            main_screen_bg.paste(
                game_logo, self.banner_info.game_logo_left_top, mask=game_logo
            )

        if self.banner_info.capcom_logo_left_top != (0, 0):
            capcom_logo_path = os.path.join(
                LocalConfigs.repository_directory(), "image\\logo\\capcom.png"
            )
            capcom_logo = Image.open(capcom_logo_path).resize(
                (S_BannerInfo.CAPCOM_LOGO_WIDTH, S_BannerInfo.CAPCOM_LOGO_HEIGHT)
            )
            main_screen_bg.paste(
                capcom_logo, self.banner_info.capcom_logo_left_top, mask=capcom_logo
            )

        main_screen_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\standard\\MenuScreen1.png",
        )
        main_screen_bg.save(main_screen_path)
