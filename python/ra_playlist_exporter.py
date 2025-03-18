# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from ra_configs import RA_Configs
from ra_playlist_header import RA_PlaylistHeader
from ra_playlist_label import RA_PlaylistLabel
from ra_playlist_path import RA_PlaylistPath
from rom_export_configs import RomExportConfigs
from rom_export_info import RomExportInfo
from ra_thumbnails_exporter import RA_ThumbnailsExporter


class RA_PlaylistExporter:
    def __init__(self, rom_export_configs: RomExportConfigs):
        self.rom_export_configs = rom_export_configs

    @staticmethod
    def __write_footer(lpl_file):
        lpl_file.write("\n  ]\n")
        lpl_file.write("}")

    def run(self):
        RA_ThumbnailsExporter(self.rom_export_configs).run()

        ra_configs = ConsoleConfigs.ra_configs()
        lpl_file_path = os.path.join(
            ConsoleConfigs.current_playlist_directory(),
            f"{ra_configs.playlist_name()}.lpl",
        )
        if os.path.exists(lpl_file_path):
            os.remove(lpl_file_path)

        if not Helper.verify_exist_directory_ex(os.path.dirname(lpl_file_path)):
            print(f"【错误】无效的目标文件 {lpl_file_path}")
            return

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            core_path = RA_PlaylistHeader.create_instance().write(lpl_file)
            playlist_lable = RA_PlaylistLabel.create_instance()
            playlist_path = RA_PlaylistPath.create_instance()

            first_rom = True

            for rom_export_info in self.rom_export_configs.rom_export_info_list():
                if first_rom:
                    first_rom = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                value = playlist_path.parse(rom_export_info.dst_path)
                lpl_file.write(f'      "path": "{value}",\n')

                value = playlist_lable.parse(rom_export_info)
                lpl_file.write(f'      "label": "{value}",\n')

                lpl_file.write(f'      "core_path": "{core_path}",\n')
                lpl_file.write(f'      "core_name": "{ra_configs.core_name()}",\n')
                lpl_file.write(f'      "crc32": "{rom_export_info.rom_crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{ra_configs.playlist_name()}.lpl"\n')
                lpl_file.write("    }")

            RA_PlaylistExporter.__write_footer(lpl_file)
            lpl_file.close()


if __name__ == "__main__":
    rom_export_configs = RomExportConfigs()
    rom_export_configs.parse()

    ra_configs = ConsoleConfigs.ra_configs()

    old_lang_code = ra_configs.lang_code()
    ra_configs.set_lang_code(RA_Configs.LANG_ZHCN)

    RA_PlaylistExporter(rom_export_configs).run()

    ra_configs.set_lang_code(old_lang_code)
