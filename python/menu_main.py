# -- coding: UTF-8 --

from menu_export_ra_files import Menu_ExportRaFiles
from menu_export_fbneo_files import Menu_ExportFBNeoFiles

from quit import Quit
from r_sam_roms_check import RSamRoms_CheckCrc32, RSamRoms_CheckTitles
# from wii_export_all import Wii_ExportAll


class MainMenu:
    __instance = None

    @staticmethod
    def instance():
        # 获取单例实例
        if MainMenu.__instance is None:
            MainMenu()
        return MainMenu.__instance

    def __init__(self):
        if MainMenu.__instance is not None:
            raise Exception("请使用 MainMenu.instance() 获取实例")
        else:
            MainMenu.__instance = self

        self.__cmd_count = 0
        self.__cmd_tip_list = {}
        self.__cmd_runner_list = {}

    def add_cmd(self, tip, runner):
        self.__cmd_count = self.__cmd_count + 1
        key = str(self.__cmd_count)

        self.__cmd_tip_list[key] = tip
        self.__cmd_runner_list[key] = runner

    def show(self):
        while True:
            print("\n\n主菜单：")
            for index in range(1, self.__cmd_count + 1):
                key = str(index)
                print(f"\t{key}. {self.__cmd_tip_list[key]}")

            input_value = str(input("\n请输入数字序号，选择要执行的操作："))
            if input_value in self.__cmd_runner_list.keys():
                self.__cmd_runner_list[input_value].run()
                print("\n操作完毕")


if __name__ == "__main__":
    main_menu = MainMenu.instance()

    Menu_ExportRaFiles.add_cmds(main_menu)

    Menu_ExportFBNeoFiles.add_cmds(main_menu)

    # Wii_ExportAll.add_cmds(main_menu)

    RSamRoms_CheckCrc32.add_cmds(main_menu)
    RSamRoms_CheckTitles.add_cmds(main_menu)

    Quit.add_cmds(main_menu)

    main_menu.show()
