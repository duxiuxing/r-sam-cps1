# -- coding: UTF-8 --

from wii_make_standard_banner import S_BannerInfo, Wii_MakeStandardBanner


if __name__ == "__main__":
    wonders3_banner_info = S_BannerInfo(
        "3wonders",
        game_logo_size=(240, 120),
        game_logo_left_top=(396, 8),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_BOTTOM,
    )

    nineteen_41_banner_info = S_BannerInfo(
        "1941",
        game_logo_size=(180, 90),
        game_logo_left_top=(410, 236),  # 右下
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    captcomm_banner_info = S_BannerInfo(
        "captcomm",
        game_logo_size=(280, 85),
        game_logo_left_top=(278, 162),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    # S1
    cawing_banner_info1 = S_BannerInfo(
        "cawing",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_BOTTOM,
    )

    # S2
    cawing_banner_info2 = S_BannerInfo(
        "cawing",
        game_logo_size=(240, 104),
        game_logo_left_top=(330, 4),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_BOTTOM,
    )

    dino_banner_info = S_BannerInfo(
        "dino",
        game_logo_size=(200, 76),
        game_logo_left_top=(20, 180),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    # S1
    ffight_banner_info1 = S_BannerInfo(
        "ffight",
        game_logo_size=(420, 210),
        game_logo_left_top=(-32, 72),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    # S2 game_logo 用的是 03.png
    ffight_banner_info2 = S_BannerInfo(
        "ffight",
        game_logo_size=(180, 152),
        game_logo_left_top=(400, 110),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_BOTTOM,
    )

    # S1
    punisher_banner_info1 = S_BannerInfo(
        "punisher",
        game_logo_size=(180, 75),
        game_logo_left_top=(404, 250),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    # S2
    punisher_banner_info2 = S_BannerInfo(
        "punisher",
        game_logo_size=(240, 100),
        game_logo_left_top=(S_BannerInfo.CAPCOM_LOGO_OFFSET_X_BOTTOM, 226),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    # S3
    punisher_banner_info3 = S_BannerInfo(
        "punisher",
        game_logo_size=(270, 112),
        game_logo_left_top=(40, 128),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    sfiii_banner_info = S_BannerInfo(
        "sfiii",
        game_logo_size=(240, 120),
        game_logo_left_top=(-24, 18),  # 左上
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_BOTTOM,
    )

    sfiii2_banner_info = S_BannerInfo(
        "sfiii2",
        game_logo_size=(240, 120),
        game_logo_left_top=(6, 208),  # 左下
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    sfiii3_banner_info = S_BannerInfo(
        "sfiii3",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    jojo_banner_info = S_BannerInfo(
        "jojo",
        game_logo_size=(160, 80),
        game_logo_left_top=(418, 250),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    jojoba_banner_info = S_BannerInfo(
        "jojoba",
        game_logo_size=(270, 150),
        game_logo_left_top=(306, 122),  # 右中
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    sfiii2_banner_info = S_BannerInfo(
        "sfiii2",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    Wii_MakeStandardBanner(punisher_banner_info3).run()
