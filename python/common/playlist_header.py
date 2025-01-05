# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from common.console_configs import ConsoleConfigs


class PlaylistHeaderBase(ABC):
    @abstractmethod
    def write(self, lpl_file):
        pass


class BlankPlaylistHeader(PlaylistHeaderBase):
    def write(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write('  "default_core_path": "",\n')
        lpl_file.write('  "default_core_name": "",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')


class WiiSdPlaylistHeader(PlaylistHeaderBase):
    def write(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(
            f'  "default_core_path": "sd:/apps/retroarch-wii/{ConsoleConfigs.ra_default_core_file_title()}_wii.dol",\n'
        )
        lpl_file.write(
            f'  "default_core_name": "{ConsoleConfigs.ra_default_core_name()}",\n'
        )
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 3,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')
