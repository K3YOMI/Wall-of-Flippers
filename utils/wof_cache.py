#!/usr/bin/python3

#                               YAao,                            
#                                 Y8888b,                        Created By: Kiyomi
#                               ,oA8888888b,                     Kiyomi: https://ko-fi.com/k3yomi
#                         ,aaad8888888888888888bo,               
#                      ,d888888888888888888888888888b,               
#                    ,888888888888888888888888888888888b,            
#                   d8888888888888888888888888888888888888,                   
#                  d888888888888888888888888888888888888888b             
#                 d888888P'                    `Y88888888Ꙩ \,          
#                 88888P'                    Ybaaaa888888  Ꙩ l          
#                a8888'                      `Y8888P' `V888888    
#              d8888888a                                `Y8888           
#             AY/'' `\Y8b                                 ``Y8b
#             Y'      `YP                                    ~~
#     _       __      ____         ____   _________                           
#    | |     / /___ _/ / /  ____  / __/  / ____/ (_)___  ____  ___  __________
#    | | /| / / __ `/ / /  / __ \/ /_   / /_  / / / __ \/ __ \/ _ \/ ___/ ___/
#    | |/ |/ / /_/ / / /  / /_/ / __/  / __/ / / / /_/ / /_/ /  __/ /  (__  )
#    |__/|__/\__,_/_/_/   \____/_/    /_/   /_/_/ .___/ .___/\___/_/  /____/
#                                              /_/   /_/


wof_data = {
    "found_flippers": [],
    "base_flippers": [],
    "live_flippers": [],
    "display_live": [],
    "display_offline": [],
    "narrow_mode": False,
    "narrow_mode_limit": 100, # Minimum number of columns for narrow mode to kick in
    "forbidden_packets_found": [],
    "all_packets_found": [],
    "max_online": 15, # Max amount of online flippers to display on the screen
    "max_offline": 15, # Max amount of offline flippers to display on the screen
    "max_ble_packets": 10, # Max amount of BLE packets to display on the screen
    "min_byte_length": 3, # Minimum amount of bytes for a packet to be considered valid
    "max_byte_length": 450, # Maximum amount of bytes to be considred suspicious
    "ble_threshold": 25, # Amount of forbidden packets to be considered a BLE attack
    "bool_isScanning": False, 
    "system_type": None,
    "forbidden_packets": [ # Not complete and feel free to add more ("_" = Random Value)
        {"PCK": "4c000719010_2055_______________", "TYPE": "BLE_APPLE_DEVICE_POPUP_CLOSE"},
        {"PCK": "4c000f05c00____________________", "TYPE": "BLE_APPLE_ACTION_MODAL_LONG"},
        {"PCK": "4c00071907_____________________", "TYPE": "BLE_APPLE_DEVICE_CONNECT"},
        {"PCK": "4c0004042a0000000f05c1__604c950", "TYPE": "BLE_APPLE_DEVICE_SETUP"},
        {"PCK": "2cfe___________________________", "TYPE": "BLE_ANDROID_DEVICE_CONNECT"},
        {"PCK": "750042098102141503210109____01_", "TYPE": "BLE_SAMSUNG_BUDS_POPUP_LONG"},
        {"PCK": "7500010002000101ff000043_______", "TYPE": "BLE_SAMSUNG_WATCH_PAIR_LONG"},
        {"PCK": "0600030080_____________________", "TYPE": "BLE_WINDOWS_SWIFT_PAIR_SHORT"},
        {"PCK": "ff006db643ce97fe427c___________", "TYPE": "BLE_LOVE_TOYS_SHORT_DISTANCE"},
    ],
    "dolphin_thinking": [ # Random quotes for the dolphin to say
        "Let's hunt some flippers", 
        "Ya'll like war driving flippers?", 
        "Skid detector 9000",
        "I'm a flipper, you're a flipper, we're all flippers!",
        "Flipper Zero : Advanced Warefare",
        "Don't be a skid!!!!!!",
        "discord.gg/squachtopia",
        "Hack the planet!",
        "Apple finally fixed their BLE crashsploit",
        "I just noticed how intimidating this ascii art is...",
        "Wall of Flippers - something something something",
	    "Now headless with commands, WallofFlippers.py -h",
        "We removed a lot of features because - it's useless now!",
    ],
    "init_directory_options": [ # Main Menu Options
        {"option": "1", "action": "Wall of Flippers", "description": "Wall of Flippers (Default)", "return": "wall_of_flippers"},
        {"option": "2", "action": "Auto-Install", "description": "Install dependencies for Wall of Flippers (Windows / (APT) Debian Linux)", "return": "install_dependencies"},
        {"option": "3", "action": "Exit", "description": "....", "return": "exit"},
    ],
    "ascii_normal": open('./ascii/normal.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
    "ascii_small": open('./ascii/small.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
}
