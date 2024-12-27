# -- coding: UTF-8 --

import os
import subprocess

from common.helper import Helper
from common.local_configs import LocalConfigs


class WiiFlow_CreateCacheFiles:
    def run(self):
        # 调用 wfc_conv.exe 生成 WiiFlow 专用的 Cache 文件（.png 格式转 .wfc 格式）
        # .wfc 格式的文件都存放在 wiiflow\\cache 文件夹里
        wfc_conv_exe_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            "pc-tool\\WFC_conv\\Windows\\wfc_conv.exe",
        )

        if not os.path.exists(wfc_conv_exe_path):
            print(f"【错误】无效的文件 {wfc_conv_exe_path}")
            zip_file_path = os.path.join(
                LocalConfigs.repository_folder_path(), "pc-tool\\WFC_conv_0-1.zip"
            )
            print(f"安装文件在 {zip_file_path}")
            return

        # wiiflow\\cache
        foler_path = os.path.join(
            LocalConfigs.repository_folder_path(), "wii\\wiiflow\\cache"
        )
        if not Helper.verify_exist_folder_ex(foler_path):
            print(f"【错误】无效的文件夹 {foler_path}")
            return

        foler_path = os.path.join(LocalConfigs.repository_folder_path(), "wii\\wiiflow")
        cmd_line = f'"{wfc_conv_exe_path}" "{foler_path}"'
        print(cmd_line)
        subprocess.call(cmd_line)


if __name__ == "__main__":
    WiiFlow_CreateCacheFiles().run()
