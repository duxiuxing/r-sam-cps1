# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath
from wii_ra_app_configs import WiiRA_AppConfigs


class WiiRA_SS_CfgExporter:
    def config_list(self):
        ra_configs = ConsoleConfigs.ra_configs()
        app_configs = ConsoleConfigs.wii_ra_app_configs()
        device_code = ConsoleConfigs.storage_device_code()

        list_ret = [
            # 目录相关的设置
            f'libretro_directory = "{device_code}:/apps/{app_configs.folder}"',
            f'screenshot_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/screenshots"',
            f'system_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/system"',
            f'extraction_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/system/temp"',
            f'savefile_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/savefiles"',
            f'savestate_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/savestates"',
            f'video_filter_dir = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/videofilters"',
            f'audio_filter_dir = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/audiofilters"',
            f'rgui_browser_directory = "{device_code}:/Games/{ra_configs.core_name()}"',
            f'overlay_directory = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/overlays"',
            f'input_overlay = "{device_code}:/private/{ra_configs.ra_ss_data_folder()}/C1MOD/overlays/..."',
            # 快捷键相关的设置
            'input_menu_combos = "1"',
            'input_load_state_axis = "-2"',
            'input_save_state_axis = "+2"',
            'input_state_slot_decrease_axis = "-3"',
            'input_state_slot_increase_axis = "+3"',
            'input_menu_toggle_axis = "nul"',
            # 界面相关的设置
            'clock_posx = "240"',
        ]

        if app_configs.remap is None:
            return list_ret

        remap_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\remaps-ra-ss\\{app_configs.remap}.txt",
        )
        if not os.path.exists(remap_file_path):
            return list_ret

        with open(remap_file_path, "r", encoding="utf-8") as remap_file:
            line = remap_file.readline()
            while line:
                if line.startswith("input_player"):
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

        if ra_configs.sys_code() != RA_Configs.SYS_WII:
            print(
                f"【错误】sys_code 当前值={ra_configs.sys_code()}，预期值={RA_Configs.SYS_WII}"
            )
            return

        if ra_configs.lang_code() != RA_Configs.LANG_EN:
            print(
                f"lang_code 当前值={ra_configs.lang_code()}，预期值={RA_Configs.LANG_EN}"
            )
            return

        app_configs = ConsoleConfigs.wii_ra_app_configs()
        if app_configs is None:
            print(
                "【错误】未调用 ConsoleConfigs.set_wii_ra_app_configs() 指定 app_configs: Wii_RaAppConfigs"
            )
            return

        dst_cfg_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"private\\{ra_configs.ra_ss_data_folder()}\\boot.dol.cfg",
        )
        if app_configs.rom_title is not None:
            dst_cfg_path = os.path.join(
                LocalConfigs.root_directory_export_to(),
                f"private\\{ra_configs.ra_ss_data_folder()}\\{app_configs.rom_title}.cfg",
            )
        if not Helper.verify_exist_directory_ex(os.path.dirname(dst_cfg_path)):
            print(f"【错误】无效的目标文件 {dst_cfg_path}")
            return
        elif os.path.exists(dst_cfg_path):
            os.remove(dst_cfg_path)

        with open(dst_cfg_path, "w", encoding="utf-8") as dst_cfg:
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
    old_sys_code = ConsoleConfigs.ra_configs().set_sys_code(RA_Configs.SYS_WII)
    old_lang_code = ConsoleConfigs.ra_configs().set_lang_code(RA_Configs.LANG_EN)

    app_configs = WiiRA_AppConfigs()
    old_app_configs = ConsoleConfigs.set_wii_ra_app_configs(app_configs)

    WiiRA_SS_CfgExporter().run()

    ConsoleConfigs.ra_configs().set_sys_code(old_sys_code)
    ConsoleConfigs.ra_configs().set_lang_code(old_lang_code)
    ConsoleConfigs.set_wii_ra_app_configs(old_app_configs)
