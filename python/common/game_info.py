# -- coding: UTF-8 --


class GameInfo:
    def __init__(self, id="", name="", en_title="", zhcn_title=""):
        self.id = id
        self.name = name
        self.en_title = en_title
        self.zhcn_title = zhcn_title
        self.rom_title = ""
        self.rom_crc32_list = set()
