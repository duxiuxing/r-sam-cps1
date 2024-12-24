# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from common.label_value import EnLabelValue
from common.path_value import WinPathValue

from ra_export_playlist import RA_ExportPlaylist
from ra_export_roms import RA_ExportFakeRoms
from ra_export_thumbnails import RA_ExportThumbnails


class RA_ExportAll:
    def __init__(self):
        self.export_roms = None
        self.playlist_name = None
        self.playlist_label_value = EnLabelValue()
        self.playlist_path_value = WinPathValue()
        self.src_boxart_folder = RA_ExportThumbnails.default_src_boxart_folder()

    def run(self):
        if self.playlist_name is None:
            print("RA_ExportAll 实例未指定 .playlist_name")
            return False

        if self.export_roms is None:
            print("RA_ExportAll 实例未指定 .export_roms")
            return False

        if self.export_roms.run() is False:
            return False

        export_playlist = RA_ExportPlaylist()
        export_playlist.export_roms = self.export_roms
        export_playlist.playlist_name = self.playlist_name        
        export_playlist.playlist_label_value = self.playlist_label_value
        export_playlist.playlist_path_value = self.playlist_path_value
        export_playlist.run()

        export_thumbnails = RA_ExportThumbnails()
        export_thumbnails.export_roms = self.export_roms
        export_thumbnails.playlist_name = self.playlist_name        
        export_thumbnails.playlist_label_value = self.playlist_label_value
        export_thumbnails.src_boxart_folder = self.src_boxart_folder
        export_thumbnails.run()
        return True


if __name__ == "__main__":
    export_all = RA_ExportAll()
    export_all.export_roms = RA_ExportFakeRoms()
    export_all.playlist_name = ConsoleConfigs.ra_default_playlist_name_en()    
    export_all.run()
