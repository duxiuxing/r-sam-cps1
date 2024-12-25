# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from PIL import Image


class WiiFlow_MakeBoxcovers:
    @staticmethod
    def boxcovers_folder_path():
        return os.path.join(
            LocalConfigs.repository_folder_path(), "wii\\wiiflow\\boxcovers"
        )

    @staticmethod
    def load_base_cover(dst_title):
        file_path = os.path.join(
            WiiFlow_MakeBoxcovers.boxcovers_folder_path(),
            ConsoleConfigs.wiiflow_plugin_name(),
            f"{dst_title}{ConsoleConfigs.rom_extension()}.png",
        )

        if not os.path.exists(file_path):
            file_path = os.path.join(
                WiiFlow_MakeBoxcovers.boxcovers_folder_path(),
                f"blank_covers\\{ConsoleConfigs.wiiflow_plugin_name()}.png",
            )
        if not os.path.exists(file_path):
            print(f"【错误】无效的文件 {file_path}")
            return None

        base_cover = Image.open(file_path)
        if base_cover.width != 1090 or base_cover.height != 680:
            print(f"【错误】非标准宽高的封面 {base_cover.width} x {base_cover.height}")
            print(file_path)
            return None
        else:
            return base_cover

    @staticmethod
    def make_boxcover(dst_title, src_paths):
        boxcover_1090x680 = WiiFlow_MakeBoxcovers.load_base_cover(dst_title)
        if boxcover_1090x680 is None:
            return

        x1 = 514
        x2 = 578

        if "front" in src_paths.keys():
            boxcover_1090x680.paste(
                Image.open(src_paths["front"]).resize(
                    (boxcover_1090x680.width - x2, boxcover_1090x680.height)
                ),
                (x2, 0),
            )

        if "back" in src_paths.keys():
            boxcover_1090x680.paste(
                Image.open(src_paths["back"]).resize((x1, boxcover_1090x680.height)),
                (0, 0),
            )

        dst_file_path = os.path.join(
            WiiFlow_MakeBoxcovers.boxcovers_folder_path(),
            f"{dst_title}{ConsoleConfigs.rom_extension()}.png",
        )
        if os.path.exists(dst_file_path):
            os.remove(dst_file_path)
        boxcover_1090x680.save(dst_file_path)

        wfc_file_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wiiflow\\cache\\{ConsoleConfigs.wiiflow_plugin_name()}",
            f"{dst_title}{ConsoleConfigs.rom_extension()}.wfc",
        )
        if os.path.exists(wfc_file_path):
            os.remove(wfc_file_path)

    def run(self):
        boxcovers_folder_path = WiiFlow_MakeBoxcovers.boxcovers_folder_path()
        if not Helper.folder_exist(boxcovers_folder_path):
            print(f"【警告】无效的文件夹 {boxcovers_folder_path}")
            return

        dst_title_to_src_paths = {}
        for file_name in os.listdir(boxcovers_folder_path):
            src_path = os.path.join(boxcovers_folder_path, file_name)
            if file_name.endswith("-front.jpg") or file_name.endswith("-front.png"):
                dst_title = file_name[:-10]
                if dst_title in dst_title_to_src_paths.keys():
                    dst_title_to_src_paths[dst_title]["front"] = src_path
                else:
                    dst_title_to_src_paths[dst_title] = {"front": src_path}
            elif file_name.endswith("-back.jpg") or file_name.endswith("-back.png"):
                dst_title = file_name[:-9]
                if dst_title in dst_title_to_src_paths.keys():
                    dst_title_to_src_paths[dst_title]["back"] = src_path
                else:
                    dst_title_to_src_paths[dst_title] = {"back": src_path}

        for dst_title, src_paths in dst_title_to_src_paths.items():
            WiiFlow_MakeBoxcovers.make_boxcover(dst_title, src_paths)


if __name__ == "__main__":
    WiiFlow_MakeBoxcovers().run()
