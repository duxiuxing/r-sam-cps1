# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from r_sam_roms import RSamRoms
from wiiflow_plugins_data import WiiFlowPluginsData


class W_BannerInfo:
    CONSOLE_LOGO_OFFSET_X_TOP = 39
    CONSOLE_LOGO_OFFSET_X_BOTTOM = 10
    CONSOLE_LOGO_OFFSET_Y_TOP = 8
    CONSOLE_LOGO_OFFSET_Y_BOTTOM = 6

    ALIGN_NONE = 0
    ALIGN_LEFT_TOP = 1
    ALIGN_LEFT_BOTTOM = 2
    ALIGN_RIGHT_TOP = 3
    ALIGN_RIGHT_BOTTOM = 4

    ALIGN_LEFT_CENTER = 5
    ALIGN_TOP_CENTER = 6
    ALIGN_RIGHT_CENTER = 7
    ALIGN_BOTTOM_CENTER = 8

    MENU_SCREEN_WIDTH = 830
    MENU_SCREEN_HEIGHT = 332

    def __init__(
        self,
        rom_title,
        game_logo_size,
        game_logo_left_top,
        console_logo_align,
        console_logo_name="01.png",
    ):
        self.rom_title = rom_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.console_logo_align = console_logo_align
        self.console_logo = None
        if self.console_logo_align != W_BannerInfo.ALIGN_NONE:
            console_logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\logo\\Console\\{console_logo_name}",
            )
            self.console_logo = Image.open(console_logo_path)

    @staticmethod
    def compute_logo_left_top(logo_size, logo_align):
        if W_BannerInfo.ALIGN_LEFT_TOP == logo_align:
            return (
                W_BannerInfo.CONSOLE_LOGO_OFFSET_X_TOP,
                W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_TOP,
            )
        elif W_BannerInfo.ALIGN_LEFT_BOTTOM == logo_align:
            return (
                W_BannerInfo.CONSOLE_LOGO_OFFSET_X_BOTTOM,
                W_BannerInfo.MENU_SCREEN_HEIGHT
                - W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_BOTTOM
                - logo_size[1],
            )
        elif W_BannerInfo.ALIGN_RIGHT_TOP == logo_align:
            return (
                W_BannerInfo.MENU_SCREEN_WIDTH
                - W_BannerInfo.CONSOLE_LOGO_OFFSET_X_TOP
                - logo_size[0],
                W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_TOP,
            )
        elif W_BannerInfo.ALIGN_RIGHT_BOTTOM == logo_align:
            return (
                W_BannerInfo.MENU_SCREEN_WIDTH
                - W_BannerInfo.CONSOLE_LOGO_OFFSET_X_BOTTOM
                - logo_size[0],
                W_BannerInfo.MENU_SCREEN_HEIGHT
                - W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_BOTTOM
                - logo_size[1],
            )
        # elif W_BannerInfo.ALIGN_LEFT_CENTER == logo_align:
        elif W_BannerInfo.ALIGN_TOP_CENTER == logo_align:
            return (
                int((W_BannerInfo.MENU_SCREEN_WIDTH - logo_size[0]) / 2),
                W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_TOP,
            )
        # elif W_BannerInfo.ALIGN_RIGHT_CENTER == logo_align:
        elif W_BannerInfo.ALIGN_BOTTOM_CENTER == logo_align:
            return (
                int((W_BannerInfo.MENU_SCREEN_WIDTH - logo_size[0]) / 2),
                W_BannerInfo.MENU_SCREEN_HEIGHT
                - W_BannerInfo.CONSOLE_LOGO_OFFSET_Y_BOTTOM
                - logo_size[1],
            )
        else:
            raise Exception(
                f"【错误】无效的取值，W_BannerInfo.logo_align = {logo_align}"
            )

    def console_logo_left_top(self):
        return W_BannerInfo.compute_logo_left_top(
            self.console_logo.size,
            self.console_logo_align,
        )


class Wii_MakeWidescreenBanner:
    def __init__(self, banner_info):
        self.banner_info = banner_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=banner_info.rom_title
        )

    def make_main_screen_bg(self):
        main_screen_bg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen-bg.png",
        )
        if os.path.exists(main_screen_bg_path):
            return Image.open(main_screen_bg_path)
        else:
            marquee_path = Helper.compute_image_path(
                self.game_info.name, "marquee", ".jpg"
            )
            image = Image.open(marquee_path).resize(
                (W_BannerInfo.MENU_SCREEN_WIDTH, W_BannerInfo.MENU_SCREEN_HEIGHT)
            )
            Helper.verify_exist_directory_ex(os.path.dirname(main_screen_bg_path))
            image.save(main_screen_bg_path, format="PNG")
            return image

    def run(self):
        main_screen_bg = self.make_main_screen_bg()
        main_screen_bg_changed = False

        if self.banner_info.game_logo_size != (0, 0):
            game_logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\logo.png",
            )
            if not os.path.exists(game_logo_path):
                game_logo_path = Helper.compute_image_path(self.game_info.name, "logo")
            game_logo = Image.open(game_logo_path).resize(
                self.banner_info.game_logo_size
            )
            main_screen_bg.paste(
                game_logo, self.banner_info.game_logo_left_top, mask=game_logo
            )
            main_screen_bg_changed = True

        if W_BannerInfo.ALIGN_NONE != self.banner_info.console_logo_align:
            main_screen_bg.paste(
                self.banner_info.console_logo,
                self.banner_info.console_logo_left_top(),
                mask=self.banner_info.console_logo,
            )
            main_screen_bg_changed = True

        if main_screen_bg_changed:
            main_screen_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen.png",
            )
            main_screen_bg.save(main_screen_path)

        main_screen_bg.resize((590, 332)).save(
            os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen1.png",
            ),
        )
