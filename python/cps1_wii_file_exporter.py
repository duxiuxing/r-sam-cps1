# -- coding: UTF-8 --

from console_configs import ConsoleConfigs
from wii_file_exporter import WiiFileExporter


if __name__ == "__main__":
    old_storage_device_code = ConsoleConfigs.set_storage_device_code(
        ConsoleConfigs.STORAGE_USB
    )
    app_type_filter = WiiFileExporter.WiiRA_App
    app_type_filter = WiiFileExporter.WiiRA_SS_App
    # app_type_filter = None
    # WiiFileExporter("FB Alpha 2012 CPS-1").run()
    # WiiFileExporter("RA-SS CPS1").run()

    # WiiFileExporter("1941 - Counter Attack", app_type_filter).run()
    # WiiFileExporter("Cadillacs and Dinosaurs", app_type_filter).run()
    # WiiFileExporter("Captain Commando", app_type_filter).run()
    # WiiFileExporter("Dynasty Wars", app_type_filter).run()
    # WiiFileExporter("JoJo's Venture").run()
    # WiiFileExporter("JoJo's Venture 2").run()
    WiiFileExporter("Street Fighter 2' CE").run()
    # WiiFileExporter("Street Fighter 3.2").run()
    # WiiFileExporter("Street Fighter 3.3").run()

    # WiiFileExporter("Final Fight", app_type_filter).run()
    # WiiFileExporter("The Punisher", app_type_filter).run()
    # WiiFileExporter("Three Wonders", app_type_filter).run()
    # WiiFileExporter("Warriors of Fate", app_type_filter).run()
    ConsoleConfigs.set_storage_device_code(old_storage_device_code)
