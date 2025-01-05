# -- coding: UTF-8 --

import fnmatch


class ConsoleConfigs:
    @staticmethod
    def short_name():
        # 机种简称
        return "CPS1"

    @staticmethod
    def rom_extension():
        return ".zip"

    @staticmethod
    def rom_extension_match(file_name):
        return fnmatch.fnmatch(file_name, "*.zip")

    @staticmethod
    def ra_default_core_name():
        # 默认的 RetroArch 核心名称
        return "Arcade (FB Alpha 2012 CPS-1)"

    @staticmethod
    def ra_default_core_file_title():
        # 默认的 RetroArch 核心文件标题
        return "fbalpha2012_cps1_libretro"

    @staticmethod
    def ra_default_playlist_name_en():
        # 默认的英文游戏列表名称
        return "R-Sam - CPS1 Arcade"

    @staticmethod
    def ra_default_playlist_name_zhcn():
        # 默认的中文游戏列表名称
        return "认真玩 - CPS1 街机"

    @staticmethod
    def wiiflow_plugin_name():
        # WiiFlow 的插件名称
        return "CPS1"
