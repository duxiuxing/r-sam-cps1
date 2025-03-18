# -- coding: UTF-8 --

import fnmatch
import os
import xml.etree.ElementTree as ET

from local_configs import LocalConfigs
from ra_configs import RA_Configs


class ConsoleConfigs:
    STORAGE_SD = "sd"
    STORAGE_USB = "usb"

    __instance = None

    def __init__(self):
        if ConsoleConfigs.__instance is not None:
            raise Exception("请使用 ConsoleConfigs._instance() 获取实例")
        else:
            ConsoleConfigs.__instance = self

        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(), "config\\console.xml"
        )
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效文件 {xml_file_path}")
        else:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            self.ra_configs = RA_Configs(root.attrib["ra_configs_file"])
            self.rom_extension = root.attrib["rom_extension"]
            self.wiiflow_plugin_name = root.attrib["wiiflow_plugin_name"]
            self.wii_ra_app_configs = None
            self.storage_device_code = ConsoleConfigs.STORAGE_SD

    @staticmethod
    def _instance():
        # 获取单例实例
        if ConsoleConfigs.__instance is None:
            ConsoleConfigs()
        return ConsoleConfigs.__instance

    @staticmethod
    def rom_extension():
        # ROM 文件的扩展名
        return ConsoleConfigs._instance().rom_extension

    @staticmethod
    def rom_extension_match(file_name):
        pat = f"*{ConsoleConfigs.rom_extension()}"
        return fnmatch.fnmatch(file_name, pat)

    @staticmethod
    def ra_configs():
        return ConsoleConfigs._instance().ra_configs

    @staticmethod
    def set_ra_configs(ra_configs):
        ret = ConsoleConfigs._instance().ra_configs
        ConsoleConfigs._instance().ra_configs = ra_configs
        return ret

    @staticmethod
    def wiiflow_plugin_name():
        # WiiFlow 的插件名称
        return ConsoleConfigs._instance().wiiflow_plugin_name

    @staticmethod
    def wii_ra_app_configs():
        return ConsoleConfigs._instance().wii_ra_app_configs

    @staticmethod
    def set_wii_ra_app_configs(wii_ra_app_configs):
        ret = ConsoleConfigs._instance().wii_ra_app_configs
        ConsoleConfigs._instance().wii_ra_app_configs = wii_ra_app_configs
        return ret

    @staticmethod
    def current_playlist_directory():
        if ConsoleConfigs._instance().ra_configs.sys_code() == RA_Configs.SYS_WII:
            app_configs = ConsoleConfigs._instance().wii_ra_app_configs
            if app_configs is not None:
                return os.path.join(
                    LocalConfigs.root_directory_export_to(),
                    f"apps\\{app_configs.folder}\\playlists",
                )

        return ConsoleConfigs._instance().ra_configs.playlist_directory()

    @staticmethod
    def storage_device_code():
        return ConsoleConfigs._instance().storage_device_code

    @staticmethod
    def set_storage_device_code(storage_device_code):
        ret = ConsoleConfigs._instance().storage_device_code
        ConsoleConfigs._instance().storage_device_code = storage_device_code
        return ret


if __name__ == "__main__":
    print(ConsoleConfigs.rom_extension())
    file_name = "test.zip"
    if ConsoleConfigs.rom_extension_match(file_name):
        print(f"{file_name} ROM 文件名匹配成功")
    else:
        print(f"{file_name} ROM 文件名不匹配")
    print(ConsoleConfigs.ra_configs().core_name())
    print(ConsoleConfigs.wiiflow_plugin_name())
