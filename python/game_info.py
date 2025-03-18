# -- coding: UTF-8 --


class GameInfo:
    def __init__(self):
        self.id = None
        self.name = None
        self.en_title = None
        self.zhcn_title = None
        self.rom_title = None
        self.rom_crc32_list = set()
        self.developer = None
        self.publisher = None
        self.genre = None
        self.date = None
        self.players = None
