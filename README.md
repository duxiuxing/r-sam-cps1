# R-Sam 认真玩 - CPS1 街机游戏


## 第三方文件说明

### Arcade - CPS1.csv

ROM 名称的中英文对照

- 本地路径：third-party > Arcade - CPS1.csv
- 项目网址：<https://github.com/duxiuxing/rom-name-cn>


### CPS1.ini 和 CPS1.xml

WiiFlow 使用的游戏数据库文件。

- 本地路径：wii > wiiflow > plugins_data > CPS1
- 介绍页面：<https://gbatemp.net/threads/wiiflow-lite.422685>
- 下载页面：<https://www.mediafire.com/file/4blrpsqqn5g0bdu/Wiiflow_Database.7z/file>


### FinalBurn Neo (ClrMame Pro XML, Arcade only).dat

XML 格式的数据库文件，描述了 FinalBurn Neo 核心支持的街机 ROM 文件。可作为数据源导入到 Romcenter APP 中使用。

- 本地路径：third-party > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat
- 项目网址：<https://github.com/libretro/FBNeo>
- 远程路径：dats > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat


### Romcenter

ROM 管理工具，可以导入 .dat 格式的数据库文件。如果 Romcenter 首次运行报错，可以把缺失的两个 .dll 文件拷贝到 firebird32 文件夹里再重试。

- 下载页面：<https://www.romcenter.com/downloadpage>
- 缺失的 .dll 文件（本地路径）：pc-tool > Romcenter > firebird32
- .dll 文件来源：<https://firebirdsql.org/en/firebird-3-0>


### FBNeo - Arcade Games.rdb

RetroArch 使用的街机游戏数据库文件。运行全能模拟器，通过“菜单 > 在线更新 > 更新数据库”，可以把 .rdb 格式的数据库文件下载到本地的 database > rdb 文件夹。

- 本地路径：third-party > FBNeo - Arcade Games.rdb
- 项目网址：<https://github.com/libretro/libretro-database>
- 远程路径：rdb > FBNeo - Arcade Games.rdb


### RDBEd

.rdb 格式的数据库文件编辑器

- 本地路径：pc-tool > RDBEd-1.4.zip
- 项目网址：<https://github.com/schellingb/RDBEd>


### wfc_conv.exe

生成 WiiFlow Cache 文件的命令行工具

- 本地路径：pc-tool > WFC_conv_0-1.zip
- 项目网址：<https://github.com/Wiimpathy/WFC_conv>
