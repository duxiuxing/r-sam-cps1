# R-Sam 认真玩 - CPS1 街机游戏


## 第三方文件说明

### image > playlist > playlist.png 和 playlist-content.png

RetraArch 使用的 CPS1 街机游戏列表图标文件。运行全能模拟器，通过“菜单 > 在线更新 > 更新素材”，可以把图标文件下载到本地的 assets > xmb > monochrome > png 文件夹。

- 项目网址：<https://github.com/libretro/retroarch-assets>
- 远程路径：xmb > monochrome > png

| 本地文件名 | 远程文件名 |
| :-- | :-- |
| playlist.png | Capcom - CP System I.png |
| playlist-content.png | Capcom - CP System I-content.png |


### pc-tool > Romcenter > firebird32

Romcenter 是一个 ROM 管理工具，可以导入 .dat 格式的数据库文件。如果 Romcenter 首次运行报错，可以把 firebird32 文件夹里的两个 .dll 文件拷贝到 Romcenter 的 firebird32 文件夹里再重试。

- 下载页面：<https://www.romcenter.com/downloadpage>
- .dll 文件来源：<https://firebirdsql.org/en/firebird-3-0>


### pc-tool > RDBEd-1.4.zip

.rdb 格式的数据库文件编辑器。

- 项目网址：<https://github.com/schellingb/RDBEd>


### pc-tool > WFC_conv_0-1.zip

生成 WiiFlow Cache 文件的命令行工具。

- 项目网址：<https://github.com/Wiimpathy/WFC_conv>


### third-party > Arcade - CPS1.csv

游戏名称的中英文对照。

- 项目网址：<https://github.com/duxiuxing/rom-name-cn>


### third-party > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat

XML 格式的数据库文件，描述了 FinalBurn Neo 核心支持的街机 ROM 文件。可作为数据源导入到 Romcenter APP 中使用。

- 项目网址：<https://github.com/libretro/FBNeo>
- 远程路径：dats > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat


### third-party > FBNeo - Arcade Games.rdb

RetroArch 使用的街机游戏数据库文件。运行全能模拟器，通过“菜单 > 在线更新 > 更新数据库”，可以把 .rdb 格式的数据库文件下载到本地的 database > rdb 文件夹。

- 项目网址：<https://github.com/libretro/libretro-database>
- 远程路径：rdb > FBNeo - Arcade Games.rdb


### wii > apps > fbalpha2012_cps1

Wii 版的 FB Alpha 2012 CPS-1 核心。

- 项目网址：<https://github.com/libretro/fbalpha2012_cps1>
- 下载页面：<https://buildbot.libretro.com/stable>


### SS-Capcom CPS-1.zip

RA-SS 是 SuperrSonic 基于 RetroArch Wii 开发的简化版本。

- RA-SS 的项目网址：<https://github.com/SuperrSonic/RA-SS>

SS-Capcom CPS-1.zip 是 RunningSnakes 基于 RA-SS 制作的独立 CPS1 街机模拟器。

- 模拟器名称：RA-SS CPS1
- 最近更新时间：2024-11-17
- APP 文件夹：wii > apps > ra-cps1
- APP 的数据文件夹：wii > private > C1MOD
- 下载页面：<https://www.mediafire.com/folder/9h2hktvgyomdt/RA-SS_Modified>


### CPS-1.zip

RunningSnakes 为 RA-SS CPS1 制作的频道，用于启动 apps > ra-cps1 文件夹里的模拟器。

- 最近更新时间：2024-11-10
- 本地路径：wii > wad > ra-cps1
- 下载页面：<https://www.mediafire.com/folder/kup4smqh4aw45/RunningSnakes_Forwarders>


### wii > wiiflow > plugins_data > CPS1

WiiFlow 使用的游戏数据库文件。

- 介绍页面：<https://gbatemp.net/threads/wiiflow-lite.422685>
- 下载页面：<https://www.mediafire.com/file/4blrpsqqn5g0bdu/Wiiflow_Database.7z/file>
