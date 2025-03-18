# -- coding: UTF-8 --

import os

from local_configs import LocalConfigs


class WiiFlow_ConvertGameSynopsis:
    def run(self):
        # wiiflow\\plugins_data 里的 .xml 文件可以配置游戏的中文摘要
        # 但 WiiFlow 在显示中文句子的时候不会自动换行，需要在每个汉字之间加上空格才能有较好的显示效果，
        # 本函数用于生成 WiiFlow 专用排版格式的游戏摘要文本，原始的摘要文本存于 game_synopsis.md，
        # 转换后的摘要文本存于 game_synopsis.wiiflow.md，需要手动合入 .xml 文件
        src_file_path = os.path.join(
            LocalConfigs.repository_directory(), "doc\\game_synopsis.md"
        )
        if not os.path.exists(src_file_path):
            return

        dst_lines = []
        with open(src_file_path, "r", encoding="utf-8") as src_file:
            for line in src_file.readlines():
                src_line = line.rstrip("\n")
                if src_line.startswith("#"):
                    dst_lines.append(src_line)
                    continue
                elif len(src_line) == 0:
                    dst_lines.append("")
                    continue
                else:
                    dst_line = ""
                    for char in src_line:
                        if len(dst_line) == 0:
                            dst_line = char
                        elif dst_line[-1] in " 、：，。《》（）【】“”":
                            dst_line += char
                        elif (
                            char
                            in " 、：，。《》（）【】“”1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        ):
                            dst_line += char
                        else:
                            dst_line += f" {char}"

                    dst_lines.append(dst_line)

        dst_file_path = os.path.join(
            LocalConfigs.repository_directory(), "doc\\game_synopsis.wiiflow.md"
        )
        with open(dst_file_path, "w", encoding="utf-8") as dst_file:
            for line in dst_lines:
                dst_file.write(f"{line}\n")


if __name__ == "__main__":
    WiiFlow_ConvertGameSynopsis().run()
