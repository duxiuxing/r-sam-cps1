# -- coding: UTF-8 --

import os

from common.console_configs import ConsoleConfigs
from common.game_info import GameInfo
from common.helper import Helper
from common.rom_info import RomInfo

from r_sam_roms import RSamRoms
from wiiflow_plugins_data import WiiFlowPluginsData


class RSamRoms_CheckCrc32:
    @staticmethod
    def add_cmds(main_menu):
        main_menu.add_cmd(
            "检查 roms 文件夹里配置的 CRC32 是否等于实际值", RSamRoms_CheckCrc32()
        )

    def run(self):
        # 检查 roms 文件夹里配置的 CRC32 是否等于实际值
        r_sam_roms = RSamRoms.instance()

        for rom_crc32, rom_info in r_sam_roms.rom_crc32_to_info_items():
            rom_path = RSamRoms.compute_rom_path(rom_info)
            rom_crc32_compute = Helper.compute_crc32(rom_path)
            if rom_crc32 != rom_crc32_compute:
                print(f"crc32 属性不一致 {rom_path}")
                print(f"\t{rom_crc32} 在 roms 文件夹里的 .xml 文件中")
                print(f"\t{rom_crc32_compute} 是实际计算出来的 crc32")
            rom_bytes_compute = str(os.stat(rom_path).st_size)
            if rom_info.rom_bytes != rom_bytes_compute:
                print(f"bytes 属性不一致 {rom_path}")
                print(f"\t{rom_info.rom_bytes} 在 roms 文件夹里的 .xml 文件中")
                print(f"\t{rom_bytes_compute} 是实际计算出来的文件大小")


class RSamRoms_CheckTitles:
    @staticmethod
    def add_cmds(main_menu):
        main_menu.add_cmd(
            "检查 roms 文件夹里配置的游戏名称是否与 WiiFlowPluginsData 的一致",
            RSamRoms_CheckTitles(),
        )

    def run(self):
        # WiiFlowPluginsData 里有当前机种所有游戏的详细信息
        # 本函数用于检查 roms 文件夹里配置的游戏名称是否与 WiiFlowPluginsData 的一致
        wiiflow_plugins_data = WiiFlowPluginsData.instance()
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        r_sam_roms = RSamRoms.instance()

        for rom_crc32, rom_info in r_sam_roms.rom_crc32_to_info_items():
            game_info = wiiflow_plugins_data.query_game_info(rom_crc32=rom_crc32)
            if game_info is None:
                print(f"{plugin_name}.ini 中缺失配置")
                print(f"{rom_info.rom_title} = {rom_info.rom_crc32}")
            else:
                if rom_info.game_name != game_info.name:
                    print("游戏名称不一致")
                    print(f"\t{rom_info.game_name} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.name} 在 {plugin_name}.xml")

                if Helper.remove_region(rom_info.en_title) != game_info.en_title:
                    print(f"rom_crc = {rom_info.rom_crc32} 的 Rom 元素 en 属性不一致")
                    print(f"\t{rom_info.en_title} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.en_title} 在 {plugin_name}.xml")

                if Helper.remove_region(rom_info.zhcn_title) != game_info.zhcn_title:
                    print(f"rom_crc = {rom_info.rom_crc32} 的 Rom 元素 zhcn 属性不一致")
                    print(f"\t{rom_info.zhcn_title} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.zhcn_title} 在 {plugin_name}.xml")
