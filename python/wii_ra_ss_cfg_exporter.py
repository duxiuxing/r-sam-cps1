# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath


class WiiRA_SS_CfgExporter:
    def __init__(self, rom_title, remap_file_title):
        ra_configs = ConsoleConfigs.ra_configs()

        self.dst_cfg_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"private\\{ra_configs.ra_ss_data_folder()}\\main.cfg",
        )
        if rom_title is not None:
            self.dst_cfg_path = os.path.join(
                LocalConfigs.root_directory_export_to(),
                f"private\\{ra_configs.ra_ss_data_folder()}\\{rom_title}.cfg",
            )

        self.remap_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\remaps-ra-ss\\{remap_file_title}.txt",
        )

    def config_list(self):
        ra_configs = ConsoleConfigs.ra_configs()
        device_code = ConsoleConfigs.storage_device_code()

        list_ret = [
            # 目录相关的设置
            f'libretro_directory = "{device_code}:/apps/{ra_configs.ra_ss_libretro_directory()}"',
            f'screenshot_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/screenshots"',
            f'system_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/system"',
            f'extraction_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/system/temp"',
            f'savefile_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/savefiles"',
            f'savestate_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/savestates"',
            f'video_filter_dir = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/videofilters"',
            f'audio_filter_dir = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/audiofilters"',
            f'rgui_browser_directory = "{device_code}:/Games/{ra_configs.core_name()}"',
            f'overlay_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/overlays"',
            f'input_overlay = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/overlays/..."',
            # 快捷键相关的设置
            'input_menu_combos = "1"',
            'input_load_state_axis = "-2"',
            'input_state_slot_decrease_axis = "-3"',
            'input_state_slot_increase_axis = "+3"',
            'input_menu_toggle_axis = "+2"',
            # 界面相关的设置
            'clock_posx = "240"',
        ]

        if not os.path.exists(self.remap_file_path):
            return list_ret

        with open(self.remap_file_path, "r", encoding="utf-8") as remap_file:
            line = remap_file.readline()
            while line:
                if line.startswith("input_"):
                    list_ret.append(line.rstrip())
                line = remap_file.readline()

        return list_ret

    def config_dict(self):
        dict_ret = {}
        for line in self.config_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    def run(self):
        ra_configs = ConsoleConfigs.ra_configs()

        if not Helper.verify_exist_directory_ex(os.path.dirname(self.dst_cfg_path)):
            print(f"【错误】无效的目标文件 {self.dst_cfg_path}")
            return
        elif os.path.exists(self.dst_cfg_path):
            os.remove(self.dst_cfg_path)

        with open(self.dst_cfg_path, "w", encoding="utf-8") as dst_cfg:
            config_dict = self.config_dict()
            src_cfg_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\private\\{ra_configs.ra_ss_data_folder()}\\main.cfg",
            )
            with open(src_cfg_path, "r", encoding="utf-8") as src_cfg:
                line = src_cfg.readline()
                while line:
                    for key, value in config_dict.items():
                        if line.startswith(key):
                            line = value + "\n"
                            break
                    dst_cfg.write(line)
                    line = src_cfg.readline()
            dst_cfg.close()


if __name__ == "__main__":
    old_device_code = ConsoleConfigs.set_storage_device_code(ConsoleConfigs.STORAGE_SD)

    WiiRA_SS_CfgExporter(None, ConsoleConfigs.wiiflow_plugin_name().lower()).run()

    ConsoleConfigs.set_storage_device_code(old_device_code)
