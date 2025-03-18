# -- coding: UTF-8 --

from console_configs import ConsoleConfigs
from ra_configs import RA_Configs
from ra_playlist_exporter import RA_PlaylistExporter
from ra_thumbnails_exporter import RA_ThumbnailsExporter
from rom_export_configs import RomExportConfigs
from rom_exporter import RomExporter


class RA_AllExporter:
    def __init__(self):
        self.rom_export_configs = None
        self.ra_configs = None

    def run(self):
        RomExporter(self.rom_export_configs).run()

        old_ra_configs = ConsoleConfigs.ra_configs()
        if self.ra_configs is not None:
            ConsoleConfigs.set_ra_configs(self.ra_configs)

        ra_configs = ConsoleConfigs.ra_configs()
        print(
            f'Exporting "{ra_configs.playlist_name()}", sys_code={ra_configs.sys_code()}, lang_code={ra_configs.lang_code()}'
        )

        RA_PlaylistExporter(self.rom_export_configs).run()
        RA_ThumbnailsExporter(self.rom_export_configs).run()

        if self.ra_configs is not None:
            ConsoleConfigs.set_ra_configs(old_ra_configs)


if __name__ == "__main__":
    ra_all_exporter = RA_AllExporter()

    rom_export_configs = RomExportConfigs()
    rom_export_configs.parse()
    ra_all_exporter.rom_export_configs = rom_export_configs

    # 导出 Windows 用的中文游戏列表
    ra_configs = RA_Configs("retroarch.xml")
    ra_configs.set_lang_code(RA_Configs.LANG_ZHCN)
    ra_configs.set_sys_code(RA_Configs.SYS_WIN)
    ra_all_exporter.ra_configs = ra_configs

    ra_all_exporter.run()
