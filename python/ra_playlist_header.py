# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from console_configs import ConsoleConfigs
from local_configs import LocalConfigs
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath, Win_PlaylistPath, XBox_PlaylistPath
from wii_ra_app_configs import WiiRA_AppConfigs


class RA_PlaylistHeader(ABC):
    @staticmethod
    def create_instance():
        sys_code = ConsoleConfigs.ra_configs().sys_code()
        if sys_code == RA_Configs.SYS_WII:
            return Wii_PlaylistHeader()
        elif sys_code == RA_Configs.SYS_WIN:
            return Win_PlaylistHeader()
        else:
            return None

    @abstractmethod
    def write(self, lpl_file):
        pass


class Wii_PlaylistHeader(RA_PlaylistHeader):
    def write(self, lpl_file):
        ra_configs = ConsoleConfigs.ra_configs()
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        core_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\{ra_configs.core_file()}",
        )
        core_path = Wii_PlaylistPath().parse(core_path)

        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(f'  "default_core_path": "{core_path}",\n')
        lpl_file.write(f'  "default_core_name": "{ra_configs.core_name()}",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 3,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

        return core_path


class Win_PlaylistHeader(RA_PlaylistHeader):
    def write(self, lpl_file):
        ra_configs = ConsoleConfigs.ra_configs()

        core_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"RetroArch-Win64\\core\\{ra_configs.core_file()}",
        )
        core_path = Win_PlaylistPath().parse(core_path)

        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(f'  "default_core_path": "{core_path}",\n')
        lpl_file.write(f'  "default_core_name": "{ra_configs.core_name()}",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

        return core_path


class Xbox_PlaylistHeader(RA_PlaylistHeader):
    def write(self, lpl_file):
        ra_configs = ConsoleConfigs.ra_configs()

        core_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"RetroArch\\core\\{ra_configs.core_file()}",
        )
        core_path = XBox_PlaylistPath().parse(core_path)

        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(f'  "default_core_path": "{core_path}",\n')
        lpl_file.write(f'  "default_core_name": "{ra_configs.core_name()}",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

        return core_path
