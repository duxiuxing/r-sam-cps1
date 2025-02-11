# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.game_info import GameInfo
from common.helper import Helper
from common.local_configs import LocalConfigs
from PIL import Image

from wiiflow_plugins_data import WiiFlowPluginsData


class BannerInfo:
    def __init__(
        self,
        rom_title,
        game_logo_size,
        game_logo_left_top,
        capcom_logo_left_top,
        wallpaper=None,
    ):
        self.rom_title = rom_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.capcom_logo_left_top = capcom_logo_left_top
        self.wallpaper = wallpaper


class Wii_MakeBanner:
    def __init__(self, banner_info):
        self.banner_info = banner_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=banner_info.rom_title
        )

    def make_banner_bg(self):
        wallpaper_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"image\\wallpaper\\{self.game_info.name}.jpg",
        )
        if self.banner_info.wallpaper is not None:
            wallpaper_path = os.path.join(
                LocalConfigs.repository_folder_path(),
                f"image\\wallpaper\\{self.banner_info.wallpaper}",
            )
        image = Image.open(wallpaper_path).resize((590, 332))

        banner_bg_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\MenuScreen1-bg.png",
        )
        Helper.verify_exist_folder_ex(os.path.dirname(banner_bg_path))
        image.save(banner_bg_path, format="PNG")
        return image

    def make_banner(self):
        banner_bg = self.make_banner_bg()

        game_logo_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"image\\logo\\{self.game_info.name}.png",
        )
        game_logo = Image.open(game_logo_path).resize(self.banner_info.game_logo_size)

        capcom_logo_path = os.path.join(
            LocalConfigs.repository_folder_path(), "image\\logo\\capcom.png"
        )
        capcom_logo = Image.open(capcom_logo_path).resize((142, 29))

        banner_bg.paste(game_logo, self.banner_info.game_logo_left_top, mask=game_logo)
        banner_bg.paste(
            capcom_logo, self.banner_info.capcom_logo_left_top, mask=capcom_logo
        )

        banner_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\MenuScreen1.png",
        )
        banner_bg.save(banner_path)


if __name__ == "__main__":
    sf2_banner_info = BannerInfo(
        "sf2",
        game_logo_size=(240, 120),
        game_logo_left_top=(-6, 208),  # 左下
        capcom_logo_left_top=(442, 297),  # 右下
    )

    sf2ce_banner_info = BannerInfo(
        "sf2ce",
        game_logo_size=(310, 167),
        game_logo_left_top=(260, 80),
        capcom_logo_left_top=(442, 297),  # 右下
        wallpaper="Street Fighter II - Ryu.jpg",
    )

    sf2hf_honda_banner_info = BannerInfo(
        "sf2hf",
        game_logo_size=(160, 90),
        game_logo_left_top=(6, 6),  # 左上
        capcom_logo_left_top=(442, 300),  # 右下
        wallpaper="Street Fighter II - Honda.jpg",
    )

    sf2hf_blanka_banner_info = BannerInfo(
        "sf2hf",
        game_logo_size=(160, 90),
        game_logo_left_top=(392, 10),  # 右上
        capcom_logo_left_top=(24, 18),  # 左上
        wallpaper="Street Fighter II - Blanka.jpg",
    )

    sfzch_banner_info = BannerInfo(
        "sfzch",
        game_logo_size=(250, 148),
        game_logo_left_top=(170, 180),  # 居中
        capcom_logo_left_top=(442, 300),  # 右下
    )
    Wii_MakeBanner(sf2hf_blanka_banner_info).make_banner()
