# -- coding: UTF-8 --

import os
import shutil
import zlib

from local_configs import LocalConfigs


class Helper:
    @staticmethod
    def compute_crc32(file_path):
        # 计算指定文件的 CRC32
        # Args:
        #     file_path (str): 文件路径，通常是游戏的 ROM 文件
        # Returns:
        #     str: 文件的 CRC32，八位大写十六进制字符串
        with open(file_path, "rb") as file:
            data = file.read()
            crc = zlib.crc32(data)
            crc32 = hex(crc & 0xFFFFFFFF)[2:].upper()
            return crc32.rjust(8, "0")

    @staticmethod
    def exist_directory(dir_path):
        # 判断指定文件夹是否存在
        # Args:
        #     dir_path (str): 待判断的文件夹路径
        # Returns:
        #     bool: 如果文件夹存在则返回 True，否则返回 False
        if os.path.isdir(dir_path):
            return True
        else:
            return False

    @staticmethod
    def verify_exist_directory(dir_path):
        # 判断指定文件夹是否存在，如果不存在则创建该文件夹
        # Args:
        #     dir_path (str): 待判断的文件夹路径，要求父文件夹必须是存在的
        # Returns:
        #     bool: 如果文件夹存在或创建成功，则返回 True，否则返回 False
        if Helper.exist_directory(dir_path):
            return True
        else:
            os.mkdir(dir_path)
            return Helper.exist_directory(dir_path)

    @staticmethod
    def verify_exist_directory_ex(dir_path):
        # 判断指定文件夹是否存在，如果不存在则逐级创建
        # Args:
        #     dir_path (str): 待判断的文件夹路径，如果父文件夹不存在会逐级创建
        # Returns:
        #     bool: 如果文件夹存在或创建成功，则返回 True，否则返回 False
        path = None
        for folder in dir_path.split("\\"):
            if path is None:
                path = folder
                if not Helper.exist_directory(path):
                    return False
            else:
                path = f"{path}\\{folder}"
                if not Helper.verify_exist_directory(path):
                    return False
        return Helper.exist_directory(dir_path)

    @staticmethod
    def copy_directory(src, dst):
        # 用递归的方式，复制文件夹
        # Args:
        #     src (str): 源文件夹路径
        #     dst (str): 目标文件夹路径
        if not Helper.verify_exist_directory_ex(dst):
            print(f"【错误】无效的目标文件夹 {dst}")
            return
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                Helper.copy_directory(s, d)
            elif not os.path.exists(d):
                shutil.copy2(s, d)

    @staticmethod
    def copy_file(src, dst):
        # 复制文件
        # Args:
        #     src (str): 源文件路径
        #     dst (str): 目标文件路径，如果父文件夹不存在会逐级创建
        if not Helper.verify_exist_directory_ex(os.path.dirname(dst)):
            print(f"【错误】无效的目标文件 {dst}")
            return
        if not os.path.exists(dst):
            if os.path.exists(src):
                shutil.copy2(src, dst)
            else:
                print(f"【错误】无效的源文件 {src}")

    @staticmethod
    def copy_file_if_not_exist(src_file_path, dst_file_path):
        # 复制源文件到目标路径，如果目标文件已存在则跳过
        # Args:
        #     src_file_path (str): 源文件路径
        #     dst_file_path (str): 目标文件路径
        if not os.path.exists(src_file_path):
            print(f"【错误】无效的源文件 {src_file_path}")
        elif not os.path.exists(dst_file_path):
            shutil.copyfile(src_file_path, dst_file_path)

    @staticmethod
    def remove_region(title):
        left_index = title.find(" (")
        if left_index == -1:
            left_index = title.find("(")
        right_index = title.rfind(")")

        if left_index != -1 and right_index != -1:
            return title.replace(title[left_index : right_index + 1], "")
        else:
            return title

    @staticmethod
    def get_rom_title(rom_name):
        return os.path.splitext(rom_name)[0]

    @staticmethod
    def get_rom_region(rom_name):
        rom_title = os.path.splitext(rom_name)[0]
        left_index = rom_title.find("(")
        right_index = rom_title.find(")")

        if left_index != -1 and right_index != -1:
            rom_region = rom_title[left_index + 1 : right_index]
            if rom_region.upper() == "CHINA" or rom_region == "中":
                return "China"
            elif rom_region.upper() == "EUROPE" or rom_region == "欧":
                return "Europe"
            elif rom_region.upper() == "USA" or rom_region == "美":
                return "USA"
            elif rom_region.upper() == "JAPAN" or rom_region == "日":
                return "Japan"
            else:
                print(f"未知的地区：{rom_region}")
                return rom_region
        else:
            return None

    @staticmethod
    def get_rom_extension(rom_name):
        return os.path.splitext(rom_name)[1]

    @staticmethod
    def files_in_letter_folder():
        # 如果 roms 文件夹里有 roms.xml，则返回 False，否则返回 True
        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(), "roms\\roms.xml"
        )
        if os.path.exists(xml_file_path):
            return False
        else:
            return True
