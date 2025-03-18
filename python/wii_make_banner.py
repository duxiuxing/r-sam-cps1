# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class BannerInfo:
    def __init__(
        self, rom_title, game_logo_size, game_logo_left_top, capcom_logo_left_top
    ):
        self.rom_title = rom_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.capcom_logo_left_top = capcom_logo_left_top


class Wii_MakeBanner:
    def __init__(self, banner_info):
        self.banner_info = banner_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=banner_info.rom_title
        )

    def make_banner_bg(self):
        banner_bg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\MenuScreen1-bg.png",
        )
        if os.path.exists(banner_bg_path):
            return Image.open(banner_bg_path)
        else:
            wallpaper_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\wallpaper\\{self.game_info.name}.jpg",
            )
            image = Image.open(wallpaper_path).resize((590, 332))
            Helper.verify_exist_directory_ex(os.path.dirname(banner_bg_path))
            image.save(banner_bg_path, format="PNG")
            return image

    def run(self):
        banner_bg = self.make_banner_bg()

        if self.banner_info.game_logo_size != (0, 0):
            game_logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\logo\\{self.game_info.name}.png",
            )
            game_logo = Image.open(game_logo_path).resize(
                self.banner_info.game_logo_size
            )
            banner_bg.paste(
                game_logo, self.banner_info.game_logo_left_top, mask=game_logo
            )

        if self.banner_info.capcom_logo_left_top != (0, 0):
            capcom_logo_path = os.path.join(
                LocalConfigs.repository_directory(), "image\\logo\\capcom.png"
            )
            capcom_logo = Image.open(capcom_logo_path).resize((142, 29))
            banner_bg.paste(
                capcom_logo, self.banner_info.capcom_logo_left_top, mask=capcom_logo
            )

        banner_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\MenuScreen1.png",
        )
        banner_bg.save(banner_path)


if __name__ == "__main__":
    three_wonders_banner_info = BannerInfo(
        "3wonders",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=(680, 290),  # 右下
    )

    nineteen_41_banner_info = BannerInfo(
        "1941",
        game_logo_size=(180, 90),
        game_logo_left_top=(410, 236),  # 右下
        capcom_logo_left_top=(26, 8),  # 左上
    )

    cworld2j_banner_info = BannerInfo(
        "cworld2j",
        game_logo_size=(120, 60),
        game_logo_left_top=(440, 8),  # 右上
        capcom_logo_left_top=(0, 0),
    )

    jojo_banner_info = BannerInfo(
        "jojo",
        game_logo_size=(160, 80),
        game_logo_left_top=(420, 250),  # 右下
        capcom_logo_left_top=(422, 8),  # 右上
    )

    jojoba_banner_info = BannerInfo(
        "jojoba",
        game_logo_size=(270, 150),
        game_logo_left_top=(306, 122),  # 右中
        capcom_logo_left_top=(422, 8),  # 右上
    )

    Wii_MakeBanner(three_wonders_banner_info).run()
