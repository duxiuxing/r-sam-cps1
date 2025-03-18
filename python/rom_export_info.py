# -- coding: UTF-8 --

from rom_info import RomInfo


class RomExportInfo(RomInfo):
    def __init__(self, rom_info):
        super().__init__(
            game_name=rom_info.game_name,
            rom_crc32=rom_info.rom_crc32,
            rom_bytes=rom_info.rom_bytes,
            rom_title=rom_info.rom_title,
            en_title=rom_info.en_title,
            zhcn_title=rom_info.zhcn_title,
        )
        self.src_path = None
        self.dst_path = None
