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
    def rom_support_custom_title():
        # 1. 支持 ROM 文件自定义命名的机种
        #   1.1 导入此类 ROM 文件时，以 DB 中的命名为准
        #   1.2 导出此类 ROM 文件时，目标文件以 export-config\\*-roms.xml 中的命名为准
        # 2. 某些机种的 ROM 文件命名是固定的，不支持自定义命名，比如 CPS1/2/3 街机
        #   2.1 导入此类 ROM 文件时，以源文件的命名为准
        #   2.2 导出此类 ROM 文件时，目标文件以 DB 中的命名为准
        return False

    @staticmethod
    def ra_default_core_name():
        # 默认的 RetroArch 核心名称
        return "Arcade (FB Alpha 2012 CPS-1)"

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
