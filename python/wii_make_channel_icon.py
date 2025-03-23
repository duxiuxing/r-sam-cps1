# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class Wii_MakeChannelIcon:
    def __init__(self, rom_title):
        self._game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=rom_title
        )

    @staticmethod
    def check_logo_left(logo, pixel_test):
        for x in range(logo.width):
            for y in range(logo.height):
                if logo.getpixel((x, y)) != pixel_test:
                    return x
        return 0

    @staticmethod
    def check_logo_top(logo, pixel_test):
        for y in range(logo.height):
            for x in range(logo.width):
                if logo.getpixel((x, y)) != pixel_test:
                    return y
        return 0

    @staticmethod
    def check_logo_right(logo, pixel_test):
        for x_offset in range(1, logo.width + 1):
            for y in range(logo.height):
                if logo.getpixel((logo.width - x_offset, y)) != pixel_test:
                    return logo.width - x_offset
        return logo.width - 1

    @staticmethod
    def check_logo_bottom(logo, pixel_test):
        for y_offset in range(1, logo.height + 1):
            for x in range(logo.width):
                if logo.getpixel((x, logo.height - y_offset)) != pixel_test:
                    return logo.height - y_offset
        return logo.height - 1

    def load_logo(self):
        logo_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self._game_info.rom_title}\\res\\logo.png",
        )
        if not os.path.exists(logo_path):
            logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\logo\\{self._game_info.name}.png",
            )
        logo = Image.open(logo_path)
        pixel_test = logo.getpixel((0, 0))

        left = Wii_MakeChannelIcon.check_logo_left(logo, pixel_test)
        top = Wii_MakeChannelIcon.check_logo_top(logo, pixel_test)
        right = Wii_MakeChannelIcon.check_logo_right(logo, pixel_test)
        bottom = Wii_MakeChannelIcon.check_logo_bottom(logo, pixel_test)

        if (
            left == 0
            and top == 0
            and right == logo.width - 1
            and bottom == logo.height - 1
        ):
            return logo

        return logo.crop((left, top, right + 1, bottom + 1))

    def run(self):
        image_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self._game_info.rom_title}\\res\\IconImage-bg.png",
        )
        icon_image = Image.open(image_path)

        logo = self.load_logo()
        new_height = 80
        top = 8
        new_width = int(logo.width * new_height / logo.height)
        if new_width > 110:
            new_width = 110
        left = int((128 - new_width) / 2)
        new_logo = logo.resize((new_width, new_height))
        icon_image.paste(new_logo, (left, top), mask=new_logo)

        image_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self._game_info.rom_title}\\res\\IconImage.png",
        )
        icon_image.save(image_path)
