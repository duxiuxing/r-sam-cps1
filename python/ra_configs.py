# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from local_configs import LocalConfigs


class RA_Configs:
    LANG_EN = "en"
    LANG_ZHCN = "zhcn"

    SYS_ANDROID = "android"
    SYS_WII = "wii"
    SYS_WIN = "win"
    SYS_XBOX = "xbox"

    def __init__(self, xml_file_name):
        self._lang = RA_Configs.LANG_EN
        self._sys = RA_Configs.SYS_WIN

        self._items = {}
        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(), f"config\\{xml_file_name}"
        )
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效文件 {xml_file_path}")
        else:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for key, value in root.attrib.items():
                self._items[key] = value

    def _get_value(self, key, default_value=None):
        return self._items.get(key, default_value)

    def lang_code(self):
        return self._lang

    def set_lang_code(self, lang_code):
        ret = self._lang
        self._lang = lang_code
        return ret

    def sys_code(self):
        return self._sys

    def set_sys_code(self, sys_code):
        ret = self._sys
        self._sys = sys_code
        return ret

    def version(self):
        return self._get_value("version")

    def release_date(self):
        return self._get_value("release_date")

    def short_description(self):
        return self._get_value("short_description")

    def core_name(self):
        return self._get_value("core_name")

    def playlist_name(self):
        return self._get_value(f"playlist_name_{self._lang}")

    def core_file(self):
        return self._get_value(f"core_file_{self._sys}")

    def ra_ss_core_file(self):
        return self._get_value(f"ra_ss_core_file_wii")

    def ra_ss_data_folder(self):
        return self._get_value(f"ra_ss_data_folder_wii")

    def assets_directory(self):
        return os.path.join(
            LocalConfigs.root_directory_export_to(),
            self._get_value(f"assets_directory_{self._sys}"),
        )

    def playlist_directory(self):
        return os.path.join(
            LocalConfigs.root_directory_export_to(),
            self._get_value(f"playlist_directory_{self._sys}"),
        )

    def remapping_directory(self):
        return os.path.join(
            LocalConfigs.root_directory_export_to(),
            self._get_value(f"remapping_directory_{self._sys}"),
        )

    def thumbnails_directory(self):
        return os.path.join(
            LocalConfigs.root_directory_export_to(),
            self._get_value(f"thumbnails_directory_{self._sys}"),
        )

    def thumbnails_filter(self):
        return self._get_value(f"thumbnails_filter_{self._sys}")


if __name__ == "__main__":
    ra_configs = RA_Configs("retroarch.xml")
    print(ra_configs.lang_code())
    print(ra_configs.sys_code())
    print(ra_configs.core_name())
    print(ra_configs.assets_directory())
    print(ra_configs.playlist_name())
    print(ra_configs.core_file())
    print(ra_configs.playlist_directory())
    print(ra_configs.thumbnails_directory())
    print(ra_configs.thumbnails_filter())
