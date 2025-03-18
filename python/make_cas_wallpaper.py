# -- coding: UTF-8 --

import os

from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class WallpaperInfo:
    BG_01 = "01"
    BG_02 = "02"

    def __init__(self, rom_title, fg_index, bg_index):
        self.rom_title = rom_title
        self.fg_index = fg_index
        self.bg_index = bg_index


class MakeCAS_Wallpaper:
    @staticmethod
    def load_bg(bg_index):
        bg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\Capcom Arcade Stadium\\{bg_index}.jpg",
        )
        return Image.open(bg_path)

    def __init__(self, boxart_info):
        self.boxart_info = boxart_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=boxart_info.rom_title
        )

    def run(self):
        bg = MakeCAS_Wallpaper.load_bg(self.boxart_info.bg_index)

        fg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\{self.boxart_info.fg_index}.jpg",
        )
        boxart_size = (1435 - 489, 1014 - 68)
        fg = Image.open(fg_path).crop((48, 48, 1262, 1032)).resize(boxart_size)

        bg.paste(fg, (489, 68))

        wallpaper_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\09.jpg",
        )
        bg.save(wallpaper_path)

    def run2(self):
        bg = MakeCAS_Wallpaper.load_bg(self.boxart_info.bg_index)

        fg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\{self.boxart_info.fg_index}.jpg",
        )
        fg = Image.open(fg_path).crop((489, 68, 1435 , 1014))

        bg.paste(fg, (489, 68))

        wallpaper_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\09.jpg",
        )
        bg.save(wallpaper_path)

    def run3(self):
        bg = MakeCAS_Wallpaper.load_bg(self.boxart_info.bg_index)

        fg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\{self.boxart_info.fg_index}.jpg",
        )
        fg = Image.open(fg_path)

        bg.paste(fg, (489, 68))

        wallpaper_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"image\\wallpaper\\{self.game_info.name}\\09.jpg",
        )
        bg.save(wallpaper_path)

if __name__ == "__main__":
    cawing_boxart_info = WallpaperInfo(
        "cawing",
        "01",
        bg_index=WallpaperInfo.BG_01,
    )

    ffight_boxart_info = WallpaperInfo(
        "ffight",
        "10",
        bg_index=WallpaperInfo.BG_02,
    )

    MakeCAS_Wallpaper(cawing_boxart_info).run3()
