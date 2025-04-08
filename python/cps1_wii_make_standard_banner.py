# -- coding: UTF-8 --

from wii_make_standard_banner import S_BannerInfo, Wii_MakeStandardBanner


if __name__ == "__main__":
    wonders3_banner_info = S_BannerInfo(
        "3wonders",
        game_logo_size=(240, 120),
        game_logo_left_top=(396, 8),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_BOTTOM,
    )

    nineteen_41_banner_info = S_BannerInfo(
        "1941",
        game_logo_size=(180, 90),
        game_logo_left_top=(410, 236),  # 右下
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    captcomm_banner_info = S_BannerInfo(
        "captcomm",
        game_logo_size=(280, 85),
        game_logo_left_top=(278, 162),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_TOP,
    )

    # S1
    cawing_banner_info1 = S_BannerInfo(
        "cawing",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )

    # S2
    cawing_banner_info2 = S_BannerInfo(
        "cawing",
        game_logo_size=(240, 104),
        game_logo_left_top=(330, 4),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_BOTTOM,
    )

    dino_banner_info = S_BannerInfo(
        "dino",
        game_logo_size=(200, 76),
        game_logo_left_top=(20, 180),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    dynwar_banner_info1 = S_BannerInfo(
        "dynwar",
        game_logo_size=(255, 80),
        game_logo_left_top=(329, 246),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    dynwar_banner_info2 = S_BannerInfo(
        "dynwar",
        game_logo_size=(220, 70),
        game_logo_left_top=(
            S_BannerInfo.CONSOLE_LOGO_OFFSET_X_TOP,
            S_BannerInfo.CONSOLE_LOGO_OFFSET_Y_TOP,
        ),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )

    # S1
    ffight_banner_info1 = S_BannerInfo(
        "ffight",
        game_logo_size=(420, 210),
        game_logo_left_top=(-32, 72),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    # S2 game_logo 用的是 03.png
    ffight_banner_info2 = S_BannerInfo(
        "ffight",
        game_logo_size=(180, 152),
        game_logo_left_top=(400, 110),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_BOTTOM,
    )

    # S1
    punisher_banner_info1 = S_BannerInfo(
        "punisher",
        game_logo_size=(180, 75),
        game_logo_left_top=(404, 250),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    # S2
    punisher_banner_info2 = S_BannerInfo(
        "punisher",
        game_logo_size=(240, 100),
        game_logo_left_top=(S_BannerInfo.CONSOLE_LOGO_OFFSET_X_BOTTOM, 226),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_TOP,
    )

    # S3
    punisher_banner_info3 = S_BannerInfo(
        "punisher",
        game_logo_size=(270, 112),
        game_logo_left_top=(40, 128),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    wof_logo_size = (240, 120)
    wof_banner_info1 = S_BannerInfo(
        "wof",
        game_logo_size=wof_logo_size,
        game_logo_left_top=S_BannerInfo.compute_logo_left_top(
            wof_logo_size, S_BannerInfo.ALIGN_RIGHT_BOTTOM
        ),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    wof_banner_info2 = S_BannerInfo(
        "wof",
        game_logo_size=wof_logo_size,
        game_logo_left_top=S_BannerInfo.compute_logo_left_top(
            wof_logo_size, S_BannerInfo.ALIGN_RIGHT_BOTTOM
        ),
        console_logo_align=S_BannerInfo.ALIGN_LEFT_TOP,
    )

    kov_logo_size = (150, 48)
    kov_banner_info2 = S_BannerInfo(
        "kov",
        game_logo_size=kov_logo_size,
        game_logo_left_top=S_BannerInfo.compute_logo_left_top(
            kov_logo_size, S_BannerInfo.ALIGN_RIGHT_TOP
        ),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_BOTTOM,
        console_logo_name="02.png",
    )

    Wii_MakeStandardBanner(kov_banner_info2).run()
