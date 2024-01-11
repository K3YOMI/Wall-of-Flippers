#                               YAao,                            
#                                 Y8888b,                        Created By: Kiyomi + Emilia (jbohack)
#                               ,oA8888888b,                     Emilia: https://ko-fi.com/emilia0001
#                         ,aaad8888888888888888bo,               Kiyomi: https://ko-fi.com/k3yomi
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


table_ctf_compeition_confiugrations = { # This is not yet complete. expect this to come later :3 (Security and cheating is a concern still but will be worked on...)
    "is_enabled": False, 
    "ctf_link": "http://xxx.xxx.xxx:80", # CTF Host Link
    "ctf_username": "xxxxxx",
    "ctf_password": "YOUR_SECRET_PASSWORD_TO_JOIN",
    "ctf_key": "YOUR_SECRET_PASSWORD_TO_JOIN",
    "my_collection": [],
    "temp_collection": [],
}
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
    ],
    "ble_attack_directory_options": [ # Bluetooth Attack Options (Some options are hardcodes like option 13 and 14....) (Credit to ECTO-1A - https://github.com/ECTO-1A/AppleJuice)
        {"option": "1", "action": "DEVICE_AIRPOD", "hex":       			(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x02, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "2", "action": "DEVICE_AIRPOD_PRO", "hex":   			(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x0e, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "3", "action": "DEVICE_AIRPOD_MAX", "hex":   			(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x0a, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "4", "action": "DEVICE_POWERBEATS", "hex":				(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x03, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "5", "action": "DEVICE_POWERBEATS_PRO", "hex": 			(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x0b, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "6", "action": "DEVICE_BEATS", "hex": 					(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x0c, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "7", "action": "DEVICE_BEATS_STUDIO_BUDS", "hex": 		(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x11, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "8", "action": "DEVICE_BEATS_FLEX", "hex": 				(0x1e, 0xff, 0x4c, 0x00, 0x07, 0x19, 0x07, 0x10, 0x20, 0x75, 0xaa, 0x30, 0x01, 0x00, 0x00, 0x45, 0x12, 0x12, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "9", "action": "DEVICE_APPLE_TV", "hex": 				(0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x01, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "10", "action":"DEVICE_NEW_IPHONE", "hex": 				(0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x09, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "11", "action":"DEVICE_NEW_NUMBER", "hex": 	            (0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x02, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "12", "action":"DEVICE_MS_SWIFT_PAIR", "hex":  		    (0x16, 0xff, 0x06, 0x00, 0x03, 0x00, 0x80, 0x57, 0x61, 0x6C, 0x6C, 0x20, 0x6F, 0x66, 0x20, 0x46, 0x6C, 0x69, 0x70, 0x70, 0x65, 0x72, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "13", "action":"DEVICE_MS_SWIFT_PAIR_CUSTOM", "hex":     (0x16, 0xff, 0x06, 0x00, 0x03, 0x00, 0x80)},
        {"option": "14", "action":"RANDOM_LOOPED", "hex": 					()}, 
        {"option": "15", "action":"LOVESPOUSE (I Think this works lol)",  "hex": (0x16, 0xff,0xff, 0x00, 0x6D, 0xB6, 0x43, 0xCE, 0x97, 0xFE, 0x42, 0x7C, 0xD5, 0x96, 0x4C, 0x03, 0x8F, 0xAE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
    ],
    "ctf_directory_options": [ # Capture the Flippers Options
        {"option": "1", "action": "Create a login", "description": "Create a login with the hosted Capture the Flippers portal"},
        {"option": "2", "action": "Start Process", "description": "Start the Capture the Flippers process"},
    ],
    "init_directory_options": [ # Main Menu Options
        {"option": "1", "action": "Wall of Flippers", "description": "Wall of Flippers (Default)", "return": "wall_of_flippers"},
        {"option": "2", "action": "Capture the Flippers (IN DEV)", "description": "Can you capture the most flippers and top the leaderboard? This is still in development. Hosting is not available right now.", "return": "capture_the_flippers"},
        {"option": "3", "action": "Advertise Bluetooth Packets", "description": "Advertise Bluetooth Packets (Linux Support Only)", "return": "advertise_bluetooth_packets"},
        {"option": "4", "action": "Auto-Install", "description": "Install dependencies for Wall of Flippers (Windows / (APT) Debian Linux)", "return": "install_dependencies"},
        {"option": "5", "action": "Exit", "description": "....", "return": "exit"},
    ],
    "ascii_normal": open('./ascii/normal.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
    "ascii_ctf_normal": open('./ascii/ctf_normal.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
    "ascii_small": open('./ascii/small.txt', 'r', encoding="utf-8").read().encode("ascii", "ignore").decode("ascii"),
}
