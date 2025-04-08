# -- coding: UTF-8 --

from wii_make_widescreen_banner import W_BannerInfo, Wii_MakeWidescreenBanner


if __name__ == "__main__":
    wonders3_banner_info = W_BannerInfo(
        "3wonders",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=(680, 290),  # 右下
    )

    nineteen_41_banner_info = W_BannerInfo(
        "1941",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_TOP,
    )

    captcomm_banner_info = W_BannerInfo(
        "captcomm",
        game_logo_size=(480, 144),
        game_logo_left_top=(175, 158),
        console_logo_align=W_BannerInfo.ALIGN_BOTTOM_CENTER,
    )

    cawing_banner_info = W_BannerInfo(
        "cawing",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_NONE,
    )

    dino_banner_info = W_BannerInfo(
        "dino",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_LEFT_TOP,
    )

    dynwar_banner_info = W_BannerInfo(
        "dynwar",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_NONE,
    )

    ffight_banner_info = W_BannerInfo(
        "ffight",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_TOP,
    )

    punisher_banner_info = W_BannerInfo(
        "punisher",
        game_logo_size=(280, 116),
        game_logo_left_top=(20, 108),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_TOP,
    )

    sf2ce_banner_info = W_BannerInfo(
        "sf2ce",
        game_logo_size=(400, 200),
        game_logo_left_top=(36, 84),  # 靠左，垂直居中
        console_logo_align=W_BannerInfo.ALIGN_LEFT_TOP,
    )

    wof_banner_info = W_BannerInfo(
        "wof",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_NONE,
    )

    kov_banner_info = W_BannerInfo(
        "wof",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_BOTTOM,
        console_logo_name="02.png",
    )

    Wii_MakeWidescreenBanner(kov_banner_info).run()
