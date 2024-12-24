# -- coding: UTF-8 --


class Quit:
    @staticmethod
    def add_cmds(main_menu):
        main_menu.add_cmd("退出程序", Quit())

    def run(self):
        exit()
