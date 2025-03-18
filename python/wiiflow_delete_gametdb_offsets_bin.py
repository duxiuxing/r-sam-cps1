# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from local_configs import LocalConfigs


class WiiFlow_DeleteGameTdbOffsetBin:
    def run(self):
        # gametdb_offsets.bin 是 WiiFlow 生成的缓存文件，删掉才会重新生成
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()
        gametdb_offsets_bin_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"wiiflow\\plugins_data\\{plugin_name}\\gametdb_offsets.bin",
        )

        if os.path.exists(gametdb_offsets_bin_path):
            os.remove(gametdb_offsets_bin_path)
