# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from r_sam_roms import RSamRoms
from ra_configs import RA_Configs
from rom_export_configs import RomExportConfigs
from rom_export_info import RomExportInfo


class RA_ThumbnailsExporter:
    @staticmethod
    def copy_image(
        rom_export_info: RomExportInfo, src_image_folder: str, dst_image_folder: str
    ):
        src_image_path = Helper.compute_image_path(
            rom_export_info.game_name, src_image_folder
        )

        ra_configs = ConsoleConfigs.ra_configs()
        dst_image_name = Helper.remove_region(rom_export_info.en_title) + ".png"
        if ra_configs.lang_code() == RA_Configs.LANG_ZHCN:
            dst_image_name = Helper.remove_region(rom_export_info.zhcn_title) + ".png"

        dst_image_path = os.path.join(
            ra_configs.thumbnails_directory(),
            ra_configs.playlist_name(),
            dst_image_folder,
            dst_image_name,
        )
        Helper.copy_file(src_image_path, dst_image_path)

    @staticmethod
    def copy_playlist_png():
        ra_configs = ConsoleConfigs.ra_configs()
        if ra_configs.sys_code() == RA_Configs.SYS_WII:
            return

        src_image_path = os.path.join(
            LocalConfigs.repository_directory(),
            "image\\playlist\\playlist.png",
        )
        dst_image_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            ra_configs.assets_directory(),
            f"xmb\\monochrome\\png\\{ra_configs.playlist_name()}.png",
        )
        Helper.copy_file(src_image_path, dst_image_path)

        src_image_path = os.path.join(
            LocalConfigs.repository_directory(),
            "image\\playlist\\playlist-content.png",
        )
        dst_image_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            ra_configs.assets_directory(),
            f"xmb\\monochrome\\png\\{ra_configs.playlist_name()}-content.png",
        )
        Helper.copy_file(src_image_path, dst_image_path)

    def __init__(self, rom_export_configs: RomExportConfigs):
        self.rom_export_configs = rom_export_configs

    def run(self):
        RA_ThumbnailsExporter.copy_playlist_png()

        r_sam_roms = RSamRoms.instance()

        ra_configs = ConsoleConfigs.ra_configs()
        thumbnails_filter = ra_configs.thumbnails_filter().split("|")

        for rom_export_info in self.rom_export_configs.rom_export_info_list():
            if "boxart" in thumbnails_filter:
                RA_ThumbnailsExporter.copy_image(
                    rom_export_info, "boxart", "Named_Boxarts"
                )

            if "disc" in thumbnails_filter:
                RA_ThumbnailsExporter.copy_image(
                    rom_export_info, "disc", "Named_Boxarts"
                )

            if "logo" in thumbnails_filter:
                RA_ThumbnailsExporter.copy_image(rom_export_info, "logo", "Named_Logos")

            if "snap" in thumbnails_filter:
                RA_ThumbnailsExporter.copy_image(rom_export_info, "snap", "Named_Snaps")

            if "title" in thumbnails_filter:
                RA_ThumbnailsExporter.copy_image(
                    rom_export_info, "title", "Named_Titles"
                )


if __name__ == "__main__":
    rom_export_configs = RomExportConfigs()
    rom_export_configs.parse()

    RA_ThumbnailsExporter(rom_export_configs).run()
