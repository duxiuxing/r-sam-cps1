# -- coding: UTF-8 --

import fnmatch
import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class LogoExporter:
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

    @staticmethod
    def crop_logo(png_path):
        logo = Image.open(png_path)
        pixel_test = logo.getpixel((0, 0))

        left = LogoExporter.check_logo_left(logo, pixel_test)
        top = LogoExporter.check_logo_top(logo, pixel_test)
        right = LogoExporter.check_logo_right(logo, pixel_test)
        bottom = LogoExporter.check_logo_bottom(logo, pixel_test)

        if (
            left == 0
            and top == 0
            and right == logo.width - 1
            and bottom == logo.height - 1
        ):
            return logo

        return logo.crop((left, top, right + 1, bottom + 1))

    def run(self):
        import_dir_path = os.path.join(
            LocalConfigs.repository_directory(), "image\\logo-import"
        )
        if not Helper.exist_directory(import_dir_path):
            print(f"【错误】无效的文件夹 {import_dir_path}")
            return

        for src_png_name in os.listdir(import_dir_path):
            if not fnmatch.fnmatch(src_png_name, "*.png"):
                continue

            src_png_path = os.path.join(import_dir_path, src_png_name)
            src_png = LogoExporter.crop_logo(src_png_path)
            if src_png.height > 300:
                new_height = 300
                new_width = int(src_png.width * new_height / src_png.height)
                dst_png = src_png.resize((new_width, new_height))
                if new_width < 600:
                    new_png = Image.new("RGBA", (600, 300), (0, 0, 0, 0))
                    left = int((600 - new_width) / 2)
                    new_png.paste(dst_png, (left, 0), mask=dst_png)
                    dst_png = new_png
            else:
                dst_png = src_png
                if dst_png.width < (dst_png.height * 2):
                    new_width = dst_png.height * 2
                    new_png = Image.new(
                        "RGBA", (new_width, dst_png.height), (0, 0, 0, 0)
                    )
                    left = int((new_width - dst_png.width) / 2)
                    new_png.paste(dst_png, (left, 0), mask=dst_png)
                    dst_png = new_png
            dst_png_path = os.path.join(import_dir_path, f"new_{src_png_name}")
            dst_png.save(dst_png_path)


if __name__ == "__main__":
    LogoExporter().run()
