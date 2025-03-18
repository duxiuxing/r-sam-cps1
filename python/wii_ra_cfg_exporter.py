# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from ra_configs import RA_Configs
from ra_playlist_path import Wii_PlaylistPath
from wii_ra_app_configs import WiiRA_AppConfigs


class WiiRA_CfgExporter:
    def config_list(self):
        ra_configs = ConsoleConfigs.ra_configs()
        app_configs = ConsoleConfigs.wii_ra_app_configs()
        device_code = ConsoleConfigs.storage_device_code()

        list_ret = [
            # 目录相关的设置
            f'thumbnails_directory = "{device_code}:/retroarch/thumbnails"',
            f'rgui_browser_directory = "{device_code}:/Games/{ra_configs.core_name()}"',
            f'playlist_directory = "{device_code}:/apps/{app_configs.folder}/playlists"',
            # 在游戏列表中显示缩略图
            'rgui_inline_thumbnails = "true"',
            'menu_thumbnails = "2"',
            'menu_left_thumbnails = "1"',
            # 在游戏过程中使用手柄的左摇杆
            'input_player1_analog_dpad_mode = "1"',
            'input_player2_analog_dpad_mode = "1"',
            'input_player3_analog_dpad_mode = "1"',
            'input_player4_analog_dpad_mode = "1"',
            'input_player5_analog_dpad_mode = "1"',
            'input_player6_analog_dpad_mode = "1"',
            'input_player7_analog_dpad_mode = "1"',
            'input_player8_analog_dpad_mode = "1"',
            # 快捷键相关的设置
            'input_menu_toggle_gamepad_combo = "4"',
            'input_load_state_axis = "-2"',
            'input_save_state_axis = "+2"',
            'input_state_slot_decrease_axis = "-3"',
            'input_state_slot_increase_axis = "+3"',
            # 精简 MAIN MENU 界面
            'menu_show_load_core = "false"',
            'menu_show_load_content = "false"',
            'menu_show_information = "false"',
            'menu_show_configurations = "false"',
            'content_show_netplay = "false"',
            # 精简 PLAYLISTS 界面
            'content_show_add_entry = "0"',
            # 'content_show_favorites = "false"',
            'content_show_explore = "false"',
            # 精简游戏的快捷菜单界面
            'menu_show_rewind = "false"',
            'quick_menu_show_set_core_association = "false"',
            'quick_menu_show_reset_core_association = "false"',
            'quick_menu_show_download_thumbnails = "false"',
            # others
            f'assets_directory = "{device_code}:/apps/{app_configs.folder}/assets"',
            f'audio_filter_dir = "{device_code}:/apps/{app_configs.folder}/filters/audio"',
            f'cheat_database_path = "{device_code}:/apps/{app_configs.folder}/cheats"',
            f'content_favorites_path = "{device_code}:/apps/{app_configs.folder}/content_favorites.lpl"',
            f'content_history_path = "{device_code}:/apps/{app_configs.folder}/content_history.lpl"',
            f'content_image_history_path = "{device_code}:/apps/{app_configs.folder}/content_image_history.lpl"',
            f'content_music_history_path = "{device_code}:/apps/{app_configs.folder}/content_music_history.lpl"',
            f'content_video_history_path = "{device_code}:/apps/{app_configs.folder}/content_video_history.lpl"',
            f'joypad_autoconfig_dir = "{device_code}:/apps/{app_configs.folder}/autoconfig"',
            f'libretro_directory = "{device_code}:/apps/{app_configs.folder}"',
            f'libretro_info_path = "{device_code}:/apps/{app_configs.folder}/info"',
            f'log_dir = "{device_code}:/retroarch/logs"',
            f'osk_overlay_directory = "{device_code}:/apps/{app_configs.folder}/overlays/keyboards"',
            f'overlay_directory = "{device_code}:/apps/{app_configs.folder}/overlays"',
            f'rgui_config_directory = "{device_code}:/retroarch/config"',
            f'savefile_directory = "{device_code}:/retroarch/savefiles"',
            f'savestate_directory = "{device_code}:/retroarch/savestates"',
            f'system_directory = "{device_code}:/retroarch/system"',
            f'video_filter_dir = "{device_code}:/apps/{app_configs.folder}/filters/video"',
        ]

        if app_configs.content_show_favorites:
            list_ret.append('content_show_favorites = "true"')
        else:
            list_ret.append('content_show_favorites = "false"')

        if app_configs.content_show_history:
            list_ret.append('content_show_history = "true"')
        else:
            list_ret.append('content_show_history = "false"')

        return list_ret

    def config_dict(self):
        dict_ret = {}
        for line in self.config_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    @staticmethod
    def export_retroarch_salamander_cfg():
        ra_configs = ConsoleConfigs.ra_configs()
        app_configs = ConsoleConfigs.wii_ra_app_configs()

        cfg_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"apps\\{app_configs.folder}\\retroarch-salamander.cfg",
        )
        if os.path.exists(cfg_path):
            os.remove(cfg_path)
        with open(cfg_path, "w", encoding="utf-8") as dst_cfg:
            core_path = os.path.join(
                LocalConfigs.root_directory_export_to(),
                f"apps\\{app_configs.folder}\\{ra_configs.core_file()}",
            )
            core_path = Wii_PlaylistPath().parse(core_path)
            dst_cfg.write(f'libretro_path = "{core_path}"\n')
            dst_cfg.close()

    @staticmethod
    def export_remap_file():
        app_configs = ConsoleConfigs.wii_ra_app_configs()
        if app_configs.remap is None:
            return

        ra_configs = ConsoleConfigs.ra_configs()
        src_rmp_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\remaps\\{app_configs.remap}.rmp",
        )
        dst_rmp_path = os.path.join(
            ra_configs.remapping_directory(),
            f"{app_configs.rom_title}.rmp",
        )
        if os.path.exists(dst_rmp_path):
            os.remove(dst_rmp_path)
        Helper.copy_file(src_rmp_path, dst_rmp_path)

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
            f"apps\\{app_configs.folder}\\retroarch.cfg",
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
                "wii\\apps\\retroarch-wii\\retroarch.cfg",
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

        WiiRA_CfgExporter.export_retroarch_salamander_cfg()
        WiiRA_CfgExporter.export_remap_file()


if __name__ == "__main__":
    old_sys_code = ConsoleConfigs.ra_configs().set_sys_code(RA_Configs.SYS_WII)
    old_lang_code = ConsoleConfigs.ra_configs().set_lang_code(RA_Configs.LANG_EN)

    app_configs = WiiRA_AppConfigs()
    app_configs.folder = "retroarch-wii"
    old_app_configs = ConsoleConfigs.set_wii_ra_app_configs(app_configs)

    WiiRA_CfgExporter().run()

    ConsoleConfigs.ra_configs().set_sys_code(old_sys_code)
    ConsoleConfigs.ra_configs().set_lang_code(old_lang_code)
    ConsoleConfigs.set_wii_ra_app_configs(old_app_configs)
