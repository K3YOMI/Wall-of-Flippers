#!/usr/bin/python3

#                               YAao,                            
#                                 Y8888b,                        Created By: Kiyomi & Emilia (jbohack)
#                               ,oA8888888b,                     Kiyomi: https://ko-fi.com/k3yomi
#                         ,aaad8888888888888888bo,               Emilia: https://ko-fi.com/emilia0001
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
import random
import time 

wof_data = {
    # Generic Cache (ignore unless you want persistent cache data, refer to -h for more info)
    "bool_isScanning": False, 
    "system_type": None,
    "found_flippers": [],
    "base_flippers": [],
    "live_flippers": [],
    "display_live": [],
    "display_offline": [],
    "cachedMessages": [],
    "narrow_mode": False,
    "badge_mode": False,
    "toggle_adveriser": False,
    "forbidden_packets_found": [],
    "all_packets_found": [],
    "nearbyWof": [],

    # Display Settings and Price Calculation
    "narrow_mode_limit": 100, # Minimum number of columns for narrow mode to kick in
    "max_online": 15, # Max amount of online flippers to display on the screen
    "max_offline": 15, # Max amount of offline flippers to display on the screen
    "flipper_volume_price": 169, # Flipper Zero Price

    # Ratelimiting for flippers (Prevent Unauthorized Spammers)
    "max_flippers_ratelimited": 3, # Max amount of flippers to be displayed in x seconds
    "ratelimit_seconds": 5, # Amount of seconds to ratelimit flippers
    "last_ratelimit": time.time(), # Last time ratelimited
    "is_ratelimited": False, # Ratelimiting flag

    # Advertising Data (Broadcast to others you're using Wall of Flippers)
    "wof_advertiser": (0x1e, 0xff, 0x2c, 0x22, 0x22, 0x22, 0x22, 0x22),
    "wof_advertiserName": f"WoF-{random.randint(1000, 9999)}",
    "wof_advertiserRaw": "2c2222222222",

    # BLE Chat Settings (Modify if you want to change the BLE Chat Advertiser)
    "wof_blechatAdvertiser": (0x1e, 0xff, 0x2c, 0x22, 0x22, 0x24, 0x24, 0x24),
    "wof_bleAdvertiserRaw": "2c2222242424",
    "wof_displayName": "WoF-Guest",

    # BLE Service UUIDs to detect flippers
    "flipper_types": {
        "00003081-0000-1000-8000-00805f9b34fb": "B", # Black
        "00003082-0000-1000-8000-00805f9b34fb": "W", # White
        "00003083-0000-1000-8000-00805f9b34fb": "T", # Transparent
    },

    # BLE Spamming Detections and Settings
    "forbidden_packets": [ # Not complete and feel free to add more ("_" = Random Value)
        {"PCK": "00001812-0000-1000-8000-00805f9b34fb", "TYPE": "BLE_HUMAN_INTERFACE_DEVICE"},
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
    "max_ble_packets": 10, # Max amount of BLE packets to display on the screen
    "min_byte_length": 3, # Minimum amount of bytes for a packet to be considered valid
    "max_byte_length": 450, # Maximum amount of bytes to be considred suspicious
    "ble_threshold": 25, # Amount of forbidden packets to be csonsidered a BLE attack

    # Selections and Quotes + Ascii Art
    "dolphin_thinking": [ # Random quotes for the dolphin to say
        "Let's hunt some flippers", 
        "Ya'll like war driving flippers?", 
        "Skid detector 9000",
        "I'm a flipper, you're a flipper, we're all flippers!",
        "Flipper Zero : Advanced Warefare",
        "Don't be a skid!!!!!!",
        "discord.gg/squachtopia",
        "Hack the planet!",
	    "Now headless with commands, WallofFlippers.py -h",
        "Nyaaaaaa",
        "Linecon + BT Settings Flood = Fixed",
        "Please do not put your flipper in wet damp areas."
    ],
    "init_directory_options": [ # Main Menu Options
        {"option": "1", "action": "Wall of Flippers", "description": "Wall of Flippers (Default)", "return": "wall_of_flippers"},
        {"option": "2", "action": "BLE Chat", "description": "Chat with others using BLE", "return": "wall_of_talking"},
        {"option": "3", "action": "Auto-Install", "description": "Install dependencies for Wall of Flippers (Windows / (APT) Debian Linux)", "return": "install_dependencies"},
        {"option": "4", "action": "Exit", "description": "....", "return": "exit"},
    ],
    "ascii_normal": open('./ascii/normal.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
    "ascii_small": open('./ascii/small.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
}
