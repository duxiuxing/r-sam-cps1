# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from console_configs import ConsoleConfigs
from local_configs import LocalConfigs
from ra_configs import RA_Configs


class RA_PlaylistPath(ABC):
    @staticmethod
    def create_instance():
        sys_code = ConsoleConfigs.ra_configs().sys_code()
        if sys_code == RA_Configs.SYS_WII:
            return Wii_PlaylistPath()
        elif sys_code == RA_Configs.SYS_WIN:
            return Win_PlaylistPath()
        else:
            return None

    @abstractmethod
    def parse(self, path):
        pass


# 把 Windows 路径转成 Android 路径
class Android_PlaylistPath(RA_PlaylistPath):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"),
            "/storage/emulated/0/Games",
        )
        return value.replace("\\", "/")


# 把 Windows 路径转成 Wii 路径
class Wii_PlaylistPath(RA_PlaylistPath):
    def parse(self, path):
        root_old = LocalConfigs.root_directory_export_to()
        root_new = f"{ConsoleConfigs.storage_device_code()}:"
        if root_old[-1] == "\\":
            root_new = f"{ConsoleConfigs.storage_device_code()}:\\"
        value = path.replace(root_old, root_new)
        return value.replace("\\", "/")


# RetraArch 要求 Windows 路径使用双反斜杠
class Win_PlaylistPath(RA_PlaylistPath):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"), "..\\Games"
        )
        return value.replace("\\", "\\\\")


# 把 Windows 路径转成 XBOX 路径
class XBox_PlaylistPath(RA_PlaylistPath):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"), "E:\\Games"
        )
        return value.replace("\\", "\\\\")
