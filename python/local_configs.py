# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET


class LocalConfigs:
    __instance = None

    def __init__(self):
        if LocalConfigs.__instance is not None:
            raise Exception("请使用 LocalConfigs._instance() 获取实例")
        else:
            LocalConfigs.__instance = self

        self._repository_directory = os.getcwd()

        xml_file_path = os.path.join(self._repository_directory, "config\\local.xml")
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效文件 {xml_file_path}")
        else:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            self._seven_zip_exe_path = root.attrib["seven_zip_exe_path"]
            index = root.attrib["root_directory_export_to_index"]
            self._root_directory_export_to = root.attrib[
                f"root_directory_export_to_{index}"
            ]

    @staticmethod
    def _instance():
        # 获取单例实例
        if LocalConfigs.__instance is None:
            LocalConfigs()
        return LocalConfigs.__instance

    @staticmethod
    def repository_directory():
        # 本地仓库路径
        return LocalConfigs._instance()._repository_directory

    @staticmethod
    def seven_zip_exe_path():
        # 本机 7z.exe 的路径
        return LocalConfigs._instance()._seven_zip_exe_path

    @staticmethod
    def root_directory_export_to():
        # 导出根目录路径
        return LocalConfigs._instance()._root_directory_export_to


if __name__ == "__main__":
    print(LocalConfigs.repository_directory())
    print(LocalConfigs.seven_zip_exe_path())
    print(LocalConfigs.root_directory_export_to())
