# -- coding: UTF-8 --

from abc import ABC, abstractmethod
from console_configs import ConsoleConfigs
from helper import Helper
from ra_configs import RA_Configs
from rom_export_info import RomExportInfo


class RA_PlaylistLabel(ABC):
    @staticmethod
    def create_instance():
        lang_code = ConsoleConfigs.ra_configs().lang_code()
        if lang_code == RA_Configs.LANG_EN:
            return En_PlaylistLabel()
        elif lang_code == RA_Configs.LANG_ZHCN:
            return Zhcn_PlaylistLabel()
        else:
            return None

    @abstractmethod
    def parse(self, rom_export_info):
        pass


class En_PlaylistLabel(RA_PlaylistLabel):
    def parse(self, rom_export_info):
        return Helper.remove_region(rom_export_info.en_title)


class Zhcn_PlaylistLabel(RA_PlaylistLabel):
    def parse(self, rom_export_info):
        return Helper.remove_region(rom_export_info.zhcn_title)
