#!/usr/bin/python3

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
 

"""

    Hello and thank you for using Wall of Flippers. I've been loving all the support and feedback! 
    Wall of Flippers (WoF) is a Python based project designed for Bluet#ooth Low Energy (BTLE) exploration. 
    Its primary functionality involves the discovery of the Flipper Zero device and the identification of potential BTLE based attacks. 
    Please keep in mind this is a work in progress and will still continue to get updates
    For Documentation and more information, please visit: https://github.com/K3YOMI/Wall-of-Flippers

    
 """



import os
import time
import asyncio
import json
import random
Scanner = None
table_ctf_compeition_confiugrations = { # This is not yet complete. expect this to come later :3 (Security and cheating is a concern still but will be worked on...)
    "is_enabled": False, 
    "ctf_link": "http://xxx.xxx.xxx.xxx:xx",
    "ctf_username": "USER_NAME_TO_USE",
    "ctf_password": "YOUR_SECRET_PASSWORD_TO_JOIN",
    "ctf_key": "YOUR_SECRET_K3Y_TO_JOIN",
    "my_collection": [],
    "temp_collection": [],
}
wof_data = {
    "found_flippers": [],
    "base_flippers": [],
    "live_flippers": [],
    "display_live": [],
    "display_offline": [],
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
        {"PCK": "4c000f05c_________000010______", "TYPE": "BLE_APPLE_IOS_CRASH_LONG"},
        {"PCK": "4c000719010_2055__________________________________________", "TYPE": "BLE_APPLE_DEVICE_POPUP_CLOSE"},
        {"PCK": "4c000f05c00_______", "TYPE": "BLE_APPLE_ACTION_MODAL_LONG"},
        {"PCK": "4c00071907____________________", "TYPE": "BLE_APPLE_DEVICE_CONNECT"},
        {"PCK": "4c0004042a0000000f05c1__604c95000010000000", "TYPE": "BLE_APPLE_DEVICE_SETUP"},
        {"PCK": "2cfe______", "TYPE": "BLE_ANDROID_DEVICE_CONNECT"},
        {"PCK": "750042098102141503210109____01__063c948e00000000c700", "TYPE": "BLE_SAMSUNG_BUDS_POPUP_LONG"},
        {"PCK": "7500010002000101ff000043__", "TYPE": "BLE_SAMSUNG_WATCH_PAIR_LONG"},
        {"PCK": "0600030080_____________________", "TYPE": "BLE_WINDOWS_SWIFT_PAIR_SHORT"},
        {"PCK": "ff006db643ce97fe427c______", "TYPE": "BLE_LOVE_TOYS_SHORT_DISTANCE"},
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
        {"option": "9", "action": "DEVICE_APPLE_TV", "hex": 				(0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x01, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00)},
        {"option": "10", "action":"DEVICE_NEW_IPHONE", "hex": 				(0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x09, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00)},
        {"option": "11", "action":"DEVICE_NEW_NUMBER", "hex": 	            (0x16, 0xff, 0x4c, 0x00, 0x04, 0x04, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc1, 0x02, 0x60, 0x4c, 0x95, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00)},
        {"option": "12", "action":"DEVICE_MS_SWIFT_PAIR", "hex":  		    (0x16, 0xff, 0x06, 0x00, 0x03, 0x00, 0x80, 0x57, 0x61, 0x6C, 0x6C, 0x20, 0x6F, 0x66, 0x20, 0x46, 0x6C, 0x69, 0x70, 0x70, 0x65, 0x72, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)},
        {"option": "13", "action":"DEVICE_MS_SWIFT_PAIR_CUSTOM", "hex":     (0x16, 0xff, 0x06, 0x00, 0x03, 0x00, 0x80)},
        {"option": "14", "action":"RANDOM_LOOPED", "hex": 					()}, 
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
    "ascii": open('ascii.txt', 'r', encoding="utf8").read(),
    "ascii_ctf": open('ascii_ctf.txt', 'r', encoding="utf8").read()  
} 
class wall_of_flippers:
    def display(str_text):
        # Load flipper data from Flipper.json
        with open('Flipper.json', 'r') as flipper_file:
            flipper_data = json.load(flipper_file)
        # Update base_flippers list with flipper data
        wof_data['base_flippers'] = [key for key in flipper_data]
        # Categorize flipper data into live and offline flippers
        for key in wof_data['base_flippers']:
            key['Name'] = key['Name'].replace("Flipper ", "")[:15]
            if 'Type' not in key:  # Add a check for the 'Type' key
                key['Type'] = "Unknown"
            if key['MAC'] in wof_data['live_flippers']:
                wof_data['display_live'].append(key)
            else:
                wof_data['display_offline'].append(key)
        # Calculate various statistics
        t_allignment = 8
        ble_spamming_macs = []
        int_total_blacklisted_packets = len(wof_data['forbidden_packets_found'])
        int_total_ble_packets = len(wof_data['all_packets_found'])
        int_online_flippers = len(wof_data['display_live'])
        int_offline_flippers = len(wof_data['display_offline'])
        # Display ASCII art
        if str_text == None or str_text == "":
            library.ascii_art(None)
        else:
            library.ascii_art(str_text)
        # Display statistics for POSIX systems
        if wof_data['system_type'] == "posix":
            print(f"Latest Forbidden Advertisements..: {int_total_blacklisted_packets}")
            print(f"Latest Advertisements............: {int_total_ble_packets}")
            if len(wof_data['all_packets_found']) > 0:
                packet_counts = {}
                addrs = []
                # Count occurrences of each packet
                for packet in wof_data['all_packets_found']:
                    pck_value = packet['PCK']
                    packet_counts[pck_value] = packet_counts.get(pck_value, 0) + 1
                # Find the most common packet
                most_common_packet = max(packet_counts, key=packet_counts.get)
                # Find unique addresses for the most common packet
                for packet in wof_data['all_packets_found']:
                    if packet['PCK'] == most_common_packet:
                        if packet['MAC'] not in addrs:
                            addrs.append(packet['MAC'])
                    if len(packet['PCK']) > wof_data['max_byte_length']:
                        wof_data['forbidden_packets_found'].append({"MAC": packet['MAC'], "PCK": packet['PCK'], "Type": f"SUSPICIOUS_PACKET (+{wof_data['max_byte_length']} bytes)"})
                print(f"Most Common Advertisement.........: {most_common_packet} ({packet_counts[most_common_packet]} packets) ({len(addrs)} unique addresses)")
                # Add a summary if there are too many unique addresses
                if len(addrs) > 5:
                    wof_data['forbidden_packets_found'].append({"MAC": str(len(addrs)) + " Unique Addresses", "PCK": most_common_packet, "Type": "SUSPICIOUS_ADVERTISEMENT"})
            else: 
                print(f"Most Common Advertisement.........: None")
            # Display forbidden packets
            if len(wof_data['forbidden_packets_found']) > 0:
                t_packets = 0
                print("\n\n[!] Wall of Flippers >> These packets may not be related to the Flipper Zero.\n")
                print(f"[NAME]\t\t\t\t\t[ADDR]\t\t   [PACKET]")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
                for key in wof_data['forbidden_packets_found']:
                    if ble_spamming_macs.count(key['MAC']) == 0:
                        ble_spamming_macs.append(key['MAC'])
                        t_packets += 1 
                        if t_packets <= wof_data['max_ble_packets']: # Max amount of packets to display on the screen
                            print(f"{key['Type'].ljust(t_allignment)}\t\t{key['MAC'].ljust(t_allignment)}  {key['PCK'].ljust(t_allignment)}")
                if int_total_blacklisted_packets > wof_data['ble_threshold']:
                    print(f"━━━━━━━━━━━━━━━━━━ Bluetooth Low Energy (BLE) Attacks Detected ({int_total_blacklisted_packets} Advertisements) ━━━━━━━━━━━━━━━━━━━━")
        else:
            print(f"━━━━━━━━━━━━━━━━━━ BLE Attack Detection is still in development for Windows. ━━━━━━━━━━━━━━━━━━━━") 
        # Display flipper statistics
        print(f"\nTotal Online.....................: {int_online_flippers}")
        print(f"Total Offline....................: {int_offline_flippers}")
        print(f"\n\n[FLIPPER]{''.ljust(t_allignment)}[ADDR]{''.ljust(t_allignment)}\t\t[FIRST]{''.ljust(t_allignment)}[LAST]\t{''.ljust(t_allignment)}[RSSI]{''.ljust(t_allignment)}\t[Detection]{''.ljust(t_allignment)}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        # Display online flippers
        if int_online_flippers > 0:
            t_live = 0
            print("(ONLINE DEVICES)".center(100))
            wof_data['display_live'] = sorted(wof_data['display_live'], key=lambda k: k['unixLastSeen'], reverse=True)
            for key in wof_data['display_live']:
                t_live += 1
                if t_live <= wof_data['max_online']:
                    key['RSSI'] = str(f"{key['RSSI']} dBm")
                    print(f"{key['Name'].ljust(t_allignment)}\t{key['MAC'].ljust(t_allignment)}\t{library.unix2Text(key['unixFirstSeen']).ljust(t_allignment)}\t{library.unix2Text(key['unixLastSeen']).ljust(t_allignment)}\t{str(key['RSSI']).ljust(t_allignment)}\t{key['Detection Type']} ({key['Type']})".ljust(t_allignment))         
                if t_live > wof_data['max_online']:
                    t_left_over = int_online_flippers - wof_data['max_online']
                    print(f"Too many <online> devices to display. ({t_left_over} devices)".center(100))
                    break 
        # Display offline flippers
        if int_offline_flippers > 0:
            t_offline = 0
            print("(OFFLINE DEVICES)".center(100))
            wof_data['display_offline'] = sorted(wof_data['display_offline'], key=lambda k: k['unixLastSeen'], reverse=True)
            for key in wof_data['display_offline']:
                t_offline += 1
                if t_offline <= wof_data['max_offline']:
                    key['RSSI'] = str(f"{key['RSSI']} dBm")  
                    print(f"{key['Name'].ljust(t_allignment)}\t{key['MAC'].ljust(t_allignment)}\t{library.unix2Text(key['unixFirstSeen']).ljust(t_allignment)}\t{library.unix2Text(key['unixLastSeen']).ljust(t_allignment)}\t{str(key['RSSI']).ljust(t_allignment)}\t{key['Detection Type']} ({key['Type']})".ljust(t_allignment))                    
                    if t_offline > wof_data['max_offline']:
                        t_left_over = int_offline_flippers - wof_data['max_offline']
                        print(f"Too many <offline> devices to display. ({t_left_over} devices)".center(100))
                        break
        # Display message if no devices detected
        if int_offline_flippers == 0 and int_online_flippers == 0:
            print("No devices detected".center(100))
        # Reset data for next display
        wof_data['display_live'] = []
        wof_data['display_offline'] = []
        wof_data['live_flippers'] = []
        wof_data['forbidden_packets_found'] = []
        wof_data['all_packets_found'] = []
        wof_data['duplicated_packets'] = []
        wof_data['base_flippers'] = []
class capture_the_flippers:
    def display(str_text):
        # Display the leaderboard and user's stats
        library.ascii_art(f"You have successfully connected to the host - Good luck!")
        leaderboard_data = []
        total_flippers_found = 0
        headers = {
            "username": table_ctf_compeition_confiugrations['ctf_username'],
            "secret-key": table_ctf_compeition_confiugrations['ctf_key'], 
            "password": table_ctf_compeition_confiugrations['ctf_password']
        }
        try:
            # Get leaderboard data from the CTF host
            http = requests.get(f"{table_ctf_compeition_confiugrations['ctf_link']}/leaderboard", headers=headers) 
            if http.status_code == 200:
                response = http.json()
                total_flippers_found = response['total_flippers']
                table_ctf_compeition_confiugrations['my_collection'] = response['my_flippers']
                response['leaderboard'] = sorted(response['leaderboard'], key=lambda k: k['score'], reverse=True)
                players_top_10 = 0
                for player in response['leaderboard']:
                    players_top_10 += 1
                    if players_top_10 >= 10: break
                    leaderboard_data.append({"name": player['username'], "score": player['score'], "flippers": player['flippers']})
                # Display global and personal flipper stats
                print(f"\nGlobal Captured: {total_flippers_found}")
                print(f"My Flippers Captuted: {len(table_ctf_compeition_confiugrations['my_collection'])}")
                print(f"TOP 10 LEADERBOARD\n".center(95))
                print(f"[RANK]\t[USERNAME]\t[CURRENT SCORE]\t[FLIPPERS CAPTURED]")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                for player in leaderboard_data:
                    if len(player['name']) > 10:
                        player['name'] = player['name'][:10] + "..."
                    print(f"{(str(leaderboard_data.index(player)+1)).ljust(8)}{player['name'].ljust(8)}\t{player['score']}\t\t{player['flippers']}")     
                print("\n\n")
                print(f"YOUR STATS\n".center(95))
                print(f"[FLIPPER]{''.ljust(7)}[ADDR]{''.ljust(8)}\t\t[Detection]{''.ljust(8)}")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                for key in table_ctf_compeition_confiugrations['my_collection']:
                    key['flippers'] = json.loads(key['flippers'])
                    if len(key['flippers']) > 0: # If there are more than 2 flippers, then the user has captured a flipper
                        for flipper in key['flippers']:
                            flipper = flipper[0]
                            flipper['Name'] = flipper['Name'].replace("Flipper ", "")
                            if len(flipper['Name']) > 15:
                                flipper['Name'] = flipper['Name'][:15]
                            print(f"{flipper['Name'].ljust(8)}\t{flipper['MAC'].ljust(8)}\t{flipper['Detection Type'].ljust(8)}")
                    else:
                        print("You have not captured any flippers yet.".center(100))
        except Exception as error:
            print(f"[!] Wall of Flippers >> Failed to connect to the CTF Host >> Possibly Offline??\nError: {error}")
class library: 
    """
            Main library of functions and throughout wall of flippers.
            Anything from displaying the main menu to sorting packets is handles in this class.
            The following functions are used in the main menu.
            Each function is called depending on the user's selection.
            The functions are used to install dependencies, advertise bluetooth packets, and exit the program.
            Honestly, I should probably in future versions move these functions to a different file for
            more organization, but I'm too lazy to do that right now! :P

    """
    def __init__():
        with open('packet_logger.txt', 'w') as all_packets_file:
            all_packets_file.write("")
        dialogue_options = wof_data['init_directory_options']
        dialogue_options_dict = {option['option']: option['return'] for option in dialogue_options}
        library.ascii_art("Please Select an option to continue")
        #Check python dependencies and display a message if they are not installed.
        try:
            import bleak # Windows BLE Package
            print(f"[✓] Bleak is installed")
        except ImportError:
            print("[X] Bleak is not installed yet, ignore if you are running under a linux system.")
        try:
            import requests # HTTP Requests
            print(f"[✓] Requests is installed")
        except ImportError:
            print("[X] Requests is not installed yet")
        try:
            import bluepy.btle # Linux BLE Package
            print(f"[✓] Bluepy is installed")
        except ImportError:
            print("[X] Bluepy is not installed yet")
        print("\n\n[#]\t[ACTION]\t\t\t  [DESCRIPTION]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\n".join([f"{option['option'].ljust(8)}{option['action'].ljust(34)}{option['description']}" for option in dialogue_options]))
        try:
            str_input = input("\n[?] Wall of Flippers >> ")
            return dialogue_options_dict.get(str_input)
        except KeyboardInterrupt:
            library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
            print("\n[!] Wall of Flippers >> Exiting...")
            exit()
    def ascii_art(str_text): # This function displays ASCII art of a dolphin and clears the console.
        os.system('cls' if wof_data['system_type'] == 'nt' else 'clear')
        s_ascii = wof_data['ascii']
        if library.in_ctf():
            # If CTF mode is enabled, switch to the CTF version of the ASCII art.
            s_ascii = wof_data['ascii_ctf']
        r_quote = random.choice(wof_data['dolphin_thinking']) if not str_text else str_text
        print(s_ascii.replace("[RANDOM_QUOTE]", r_quote))
    def in_ctf(): # This function returns whether or not CTF mode is enabled.
        return table_ctf_compeition_confiugrations['is_enabled'] # Self explanatory
    def unix2Text(s_raw): # This function converts a unix timestamp to a human readable format.
        current_timestamp = int(time.time())
        t_different = current_timestamp - s_raw
        t_minutes, t_seconds = divmod(t_different, 60)
        if t_minutes > 1000:
            t_minutes = ">999"
        return f"{t_minutes}m {t_seconds}s"
    def t_log_packet(s_table): # This function logs ALL packets to a txt file (Temporarily)
        with open('packet_logger.txt', 'a') as all_packets_file:
            all_packets_file.write(f"{json.dumps(s_table, indent=4)}\n")
    def log(s_table): # This function logs the flipper data to Flipper.json
        with open('Flipper.json', 'r') as flipper_file: # Load flipper data from Flipper.json
            flipper_data = json.load(flipper_file)
        for s_flipper in flipper_data:
            if s_flipper["MAC"] == s_table["MAC"]:
                s_flipper.update({ # Update the flipper data
                    'RSSI': str(s_table['RSSI']),
                    'Detection Type': s_table['Detection Type'],
                    'unixLastSeen': s_table['unixLastSeen'],
                    'Name': s_table['Name'],
                    'Type': s_table['Type'],
                })
                break
        else:
            flipper_data.append({ # Add the flipper data
                "Name": s_table['Name'],
                "RSSI": s_table['RSSI'],
                "MAC": s_table['MAC'],
                "Detection Type": s_table['Detection Type'],
                "unixLastSeen": s_table['unixLastSeen'],
                "unixFirstSeen": s_table['unixFirstSeen'],
                "Type": s_table['Type'],
                "UUID": s_table['UUID'],
            })
        with open('Flipper.json', 'w') as flipper_file: # Save the flipper data to Flipper.json
            json.dump(flipper_data, flipper_file, indent=4)     
    def sort_packets(ble_packets): # This function sorts the BLE packets into a list of dictionaries.
        bool_flipper_discovered = False
        table_flippers_discovered = []
        table_latest_discovered = []
        bool_ctf = library.in_ctf()
        table_forbidden_packets_list = wof_data['forbidden_packets']
        for adv in ble_packets:
            Advertisement_name = adv['Name']
            Advertisement_type = adv['Type']
            Advertisement_rssi = adv['RSSI']
            Advertisement_mac = adv['MAC']
            Advertisement_packets = adv['PCK']
            Advertisement_uuid = adv['UUID']
            Advertisement_blacklist_check = None
            if not bool_ctf:
                for indiv_packet in Advertisement_packets:
                    for packet in table_forbidden_packets_list:
                        bool_similar = all(p1 == p2 or p2 == "_" for p1, p2 in zip(indiv_packet, packet['PCK']))
                        if bool_similar:
                            int_total_underscores = packet['PCK'].count("_")
                            int_total_found = sum(p != "_" for p in indiv_packet)
                            int_get_non_underscore = len(packet['PCK']) - int_total_underscores
                            if int_total_found >= int_get_non_underscore:
                                wof_data['forbidden_packets_found'].append({
                                    "Type": packet['TYPE'],
                                    "PCK": indiv_packet,
                                    "MAC": Advertisement_mac,
                                })
                        if len(indiv_packet) > wof_data['min_byte_length']: # If the packet is longer than the minimum byte length, then it is a valid packet we want to log
                            wof_data['all_packets_found'].append({
                                "PCK": indiv_packet,
                                "MAC": Advertisement_mac,
                            })
            library.t_log_packet(adv)
            if Advertisement_name.lower().startswith("flipper"):
                int_recorded = int(time.time())
                wof_data['found_flippers'] = [flipper for flipper in wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
                t_data = {
                    "Name": Advertisement_name,
                    "RSSI": Advertisement_rssi,
                    "MAC": Advertisement_mac,
                    "Detection Type": "Name",
                    "unixLastSeen": int_recorded,
                    "unixFirstSeen": int_recorded,
                    "Type": Advertisement_type,
                    "UUID": Advertisement_uuid,
                }
                if Advertisement_mac not in [flipper['MAC'] for flipper in wof_data['found_flippers']]:
                    wof_data['found_flippers'].append(t_data)
                    wof_data['live_flippers'].append(t_data["MAC"])
                    library.log(t_data)
                    bool_flipper_discovered = True
                    table_flippers_discovered.append(t_data)
                    table_latest_discovered = t_data
            elif any(Advertisement_mac.startswith(addr) for addr in ("80:e1:26", "80:e1:27")): # Credit to @elliotwutingfeng (https://github.com/elliotwutingfeng) for this fix
                int_recorded = int(time.time())
                wof_data['found_flippers'] = [flipper for flipper in wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
                t_data = {
                    "Name": Advertisement_name,
                    "RSSI": Advertisement_rssi,
                    "MAC": Advertisement_mac,
                    "Detection Type": "Address",
                    "unixLastSeen": int_recorded,
                    "unixFirstSeen": int_recorded,
                    "Type": Advertisement_type,
                    "UUID": Advertisement_uuid,
                }
                if Advertisement_mac not in [flipper['MAC'] for flipper in wof_data['found_flippers']]:
                    wof_data['found_flippers'].append(t_data)
                    wof_data['live_flippers'].append(t_data["MAC"])
                    library.log(t_data)
                    bool_flipper_discovered = True
                    table_flippers_discovered.append(t_data)
                    table_latest_discovered = t_data
            elif Advertisement_uuid != "NOT FOUND":
                int_recorded = int(time.time())
                wof_data['found_flippers'] = [flipper for flipper in wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
                t_data = {
                    "Name": Advertisement_name,
                    "RSSI": Advertisement_rssi,
                    "MAC": Advertisement_mac,
                    "Detection Type": "Identifier",
                    "unixLastSeen": int_recorded,
                    "unixFirstSeen": int_recorded,
                    "UUID": Advertisement_uuid,
                    "Type": Advertisement_type
                }
                if Advertisement_mac not in [flipper['MAC'] for flipper in wof_data['found_flippers']]:
                    wof_data['found_flippers'].append(t_data)
                    wof_data['live_flippers'].append(t_data["MAC"])
                    library.log(t_data)
                    bool_flipper_discovered = True
                    table_flippers_discovered.append(t_data)
                    table_latest_discovered = t_data
        if not bool_ctf:
            if not bool_flipper_discovered:
                wall_of_flippers.display(None)
            else:
                latest_name = table_latest_discovered['Name']
                latest_mac = table_latest_discovered['MAC']
                wall_of_flippers.display(f"I've found a wild {latest_name} ({latest_mac})")
        elif bool_ctf:
            if len(table_flippers_discovered) > 0:
                bool_alreadylogged = False 
                for flippers in table_ctf_compeition_confiugrations['temp_collection']:
                    if flippers == table_flippers_discovered[0]['MAC']:
                        bool_alreadylogged = True
                if not bool_alreadylogged:
                    table_ctf_compeition_confiugrations['temp_collection'].append(table_flippers_discovered[0]['MAC'])
                    http_header = {
                        "username": table_ctf_compeition_confiugrations['ctf_username'],
                        "secret-key": table_ctf_compeition_confiugrations['ctf_key'],
                        "password": table_ctf_compeition_confiugrations['ctf_password'],
                        "flippers": json.dumps(table_flippers_discovered)
                    }
                    try:
                        http = requests.post(f"{table_ctf_compeition_confiugrations['ctf_link']}/send-flipper-data", headers=http_header) # This can be exploited on so many levels, but I'll find a better way ehhehe (Just a simple demo)
                    except Exception as error:
                        print(f"[!] Wall of Flippers >> Failed to send flipper data to the CTF Host >> Possibly Offline??\nError: {error}")
        else: # If the system type is not supported, display an error message
            print("[!] Wall of Flippers >> Error: Type not supported")
        wof_data['bool_isScanning'] = False
    async def detection_async(os):
        wof_data['bool_isScanning'] = True
        ble_packets = []
        if os == "nt": # Windows Detection
            devices = await BleakScanner.discover()
            if devices:
                for device in devices:
                    Advertisement_name = str(device.name)
                    Advertisement_addr = str(device.address.lower())
                    Advertisement_rssi = str(device.rssi)
                    device.metadata.get("manufacturer_data", "TO_DO_LATER_NO_YET_SUPPORTED")
                    ble_packets.append({
                        "Name": Advertisement_name,
                        "MAC": Advertisement_addr,
                        "RSSI": Advertisement_rssi,
                        "PCK": "NOT FOUND",
                        "UUID": "NOT FOUND",
                        "Manufacturer": "NOT FOUND",
                        "Type": "NOT FOUND"
                    })
            else:
                wof_data['bool_isScanning'] = False
        elif os == "posix": # Linux Detection
            scanner = Scanner()
            devices = scanner.scan(5) # Scan the area for 5 seconds....
            if devices:
                for device in devices:
                    scan_list = device.getScanData()
                    device_packets = []
                    device_name = "NOT FOUND"
                    device_manufacturer = "NOT FOUND"
                    device_uuid = "NOT FOUND"
                    device_type = "NOT FOUND"
                    device_formatted = []
                    for scan_list_item in scan_list:
                        device_formatted.append({"ADTYPE": scan_list_item[0], "Description": scan_list_item[1], "Value": scan_list_item[2]})
                    for i_data in device_formatted:
                        if i_data['Description'] == "Complete Local Name":
                            device_name = i_data['Value']
                        if i_data['Description'] == "Manufacturer":
                            device_manufacturer = i_data['Value']
                        if i_data['Value'] == "00003082-0000-1000-8000-00805f9b34fb": # White Flipper
                            device_uuid = i_data['Value']
                            device_type = "White"
                        if i_data['Value'] == "00003081-0000-1000-8000-00805f9b34fb": # Black Flipper
                            device_uuid = i_data['Value']
                            device_type = "Black"
                        if i_data['Value'] == "00003083-0000-1000-8000-00805f9b34fb": # Transparent Flipper
                            device_uuid = i_data['Value']
                            device_type = "Transparent"
                        device_packets.append(i_data['Value'])
                    ble_packets.append({
                        "Name": device_name,
                        "MAC": device.addr,
                        "RSSI": device.rssi,
                        "PCK": device_packets,
                        "UUID": device_uuid,
                        "Manufacturer": device_manufacturer,
                        "Type": device_type
                    })
            else:
                wof_data['bool_isScanning'] = False
        else: # Unsupported OS
            print("[!] Wall of Flippers >> Error: Type not supported")
            wof_data['bool_isScanning'] = False
            return None
        library.sort_packets(ble_packets)
os.system("clear || cls")
wof_data['system_type'] = os.name
selection_box = library.__init__()
if selection_box == "wall_of_flippers" or selection_box == "capture_the_flippers":
    try:
        if wof_data['system_type'] == "nt":
            from bleak import BleakScanner  # Windows BLE Package
        if wof_data['system_type'] == "posix":
            from bluepy.btle import Scanner  # Linux BLE Package
        import requests
    except Exception as error:
        library.ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {error}")
        exit()
if selection_box == 'wall_of_flippers':
    print("[!] Wall of Flippers >> Starting Wall of Flippers")
    if wof_data['system_type'] == "posix" and not os.geteuid() == 0:
        library.ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        exit()  # Check if the user is root (Linux)
    wall_of_flippers.display("Thank you for using Wall of Flippers")
    try:
        while True:
            if not wof_data['bool_isScanning']:
                asyncio.run(library.detection_async(wof_data['system_type']))
            time.sleep(1)
    except KeyboardInterrupt:
        library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        exit()
if selection_box == 'capture_the_flippers':
    if wof_data['system_type'] == "posix" and os.geteuid() != 0:
        library.ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        exit()  # Check if the user is root (Linux)
    table_ctf_compeition_confiugrations['is_enabled'] = True
    url = table_ctf_compeition_confiugrations['ctf_link']
    password = table_ctf_compeition_confiugrations['ctf_password']
    key = table_ctf_compeition_confiugrations['ctf_key']
    username = table_ctf_compeition_confiugrations['ctf_username']
    dialogue_options = wof_data['ctf_directory_options']
    library.ascii_art("Please select an option to continue")
    print(f"\n\n[#]\t[ACTION]\t\t\t  [DESCRIPTION]")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for option in dialogue_options:
        print(f"{option['option'].ljust(8)}{option['action'].ljust(34)}{option['description']}")
    user_input = input("[?] Wall of Flippers >> ")
    for option in dialogue_options:
        if user_input == option['option']:
            if option['option'] == "1":
                library.ascii_art("Please create a username so the host can create an account")
                input_username = input("\n[?] Wall of Flippers >> Username: ")
                headers = {"username": input_username, "password": password}
                try:
                    http = requests.post(f"{url}/create_account", headers=headers)
                    if http.status_code == 400:  # Already exists
                        response = http.json()
                        library.ascii_art(f"Capture the Flippers >> Error: {response['error']}")
                        print(f"\n[!] Capture the Flippers >> Error: {response['error']}")
                    if http.status_code == 403:  # Password Failed
                        response = http.json()
                        library.ascii_art(f"Capture the Flippers >> Error: {response['error']} {response['message']}")
                        print(f"\n[!] Capture the Flippers >> Error: {response['error']} {response['message']}")
                    if http.status_code == 200:  # Success
                        response = http.json()
                        library.ascii_art(
                            f"You can now participate in the hosted Capture the Flippers event: Key = {response['secret-key-created']}")
                        print(f"\n[!] Capture the Flippers >> Your unique key is: {response['secret-key-created']}")
                        print(f"[!] Capture the Flippers >> Please save this key as you will need it to login.")
                except Exception as error:
                    print(
                        f"[!] Capture the Flippers >> Error: Failed to connect to the CTF Host >> Create Account Failed\nError: {error}")
            if option['option'] == "2":
                headers = {"username": username, "secret-key": key, "password": password}
                try:
                    http = requests.post(f"{url}/login", headers=headers)
                    if http.status_code == 403:  # Authorization Failed
                        response = http.json()
                        library.ascii_art(f"Capture the Flippers >> Error: {response['error']} {response['message']}")
                        print(f"\n[!] Capture the Flippers >> Error: {response['error']} {response['message']}")
                    if http.status_code == 200:  # Success
                        library.ascii_art(f"You have successfully connected to the host - Good luck!")
                        time.sleep(0.4)
                        try: 
                            while True:
                                if not wof_data['bool_isScanning']:
                                    capture_the_flippers.display("You have successfully connected to the host - Good luck!")
                                    asyncio.run(library.detection_async(wof_data['system_type']))
                                time.sleep(1)  # Don't worry about this - Everything is fine... :P
                        except KeyboardInterrupt:
                            library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
                            print("\n[!] Wall of Flippers >> Exiting...")
                            exit()
                except Exception as error:
                    print(
                        f"[!] Capture the Flippers >> Error: Failed to connect to the CTF Host >> Login Failed\nError: {error}")
if selection_box == 'advertise_bluetooth_packets':
    if not wof_data['system_type'] == "posix":
        library.ascii_art("This feature is not supported on your device.")
        print("[!] Wall of Flippers >> This feature is not supported on your device.")
        exit()
    try:
        from utils.bluetooth_utils import toggle_device, start_le_advertising, stop_le_advertising
        import bluetooth._bluetooth as bluez
    except Exception as error:
        library.ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {error}")
        exit()
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        toggle_device(dev_id, True)
    except Exception as error:
        library.ascii_art("Error: Failed to open bluetooth device")
        print(f"[!] Wall of Flippers >> Failed to open bluetooth device {dev_id}\nError: {error}")
        exit()
    library.ascii_art(f"Please Select an option to continue")
    print(f"\n\n[#]\t[ACTION]")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    dialogue_options = wof_data['ble_attack_directory_options'] # Credits for the directory @ECTO-1A (https://github.com/ECTO-1A/AppleJuice)
    for option in dialogue_options:
        print(f"{option['option'].ljust(8)}{option['action'].ljust(34)}")
    try:
        user_input = input("[?] Wall of Flippers >> ")
        if user_input == "13":
            user_input_custom = input("[?] Wall of Flippers >> Please enter a custom message >> ")
            data_hex = lambda data: ''.join(f"{i:02x}" for i in data)
            dialogue_options[12]['hex'] = (0x16, 0xff, 0x06, 0x00, 0x03, 0x00, 0x80) + tuple(user_input_custom.encode())
            while len(dialogue_options[12]['hex']) < 31:
                dialogue_options[12]['hex'] += (0x00,)
            if len(dialogue_options[12]['hex']) > 31:
                dialogue_options[12]['hex'] = dialogue_options[12]['hex'][:31]
        elif user_input == "14":
            try:
                while True:
                    time.sleep(0.1)
                    random_data = dialogue_options[random.randint(0, len(dialogue_options) - 2)]
                    if random_data['action'] != "RANDOM_LOOPED":
                        data = random_data['hex']
                        to_hex = lambda data: ''.join(f"{i:02x}" for i in data)
                        data_hex = to_hex(data)
                        start_le_advertising(sock, adv_type=0x03, data=data)
                        time.sleep(0.1)
                        print(f"Wall of Flippers >> Advertising as {random_data['action']} >> {data_hex}")
                        stop_le_advertising(sock)  # Make sure this function is correctly implemented
            except KeyboardInterrupt:
                stop_le_advertising(sock)
                library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
                exit()
        if not user_input == "14":
            for option in dialogue_options:
                if user_input == option['option'] and option['action'] != "RANDOM_LOOPED":
                    library.ascii_art("Advertising as " + option['action'])
                    data = option['hex']
                    to_hex = lambda data: ''.join(f"{i:02x}" for i in data)
                    try:
                        while True:
                            start_le_advertising(sock, adv_type=0x03, data=data)
                            print(f"Wall of Flippers >> Advertising as {option['action']} >> {to_hex}")
                            time.sleep(0.1)
                            stop_le_advertising(sock)  # Make sure this function is correctly implemented
                    except KeyboardInterrupt:
                        stop_le_advertising(sock)
                        library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
                        exit() # test
    except KeyboardInterrupt:
        library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        exit()
if selection_box == 'install_dependencies':
    try:
        library.ascii_art("Welcome to the easy install process! Please read carefully.")
        linux_dependencies_cmd = ['sudo apt-get install python3-pip', 'sudo apt-get install libglib2.0-dev', 'pip install bluepy', 'pip install requests']
        windows_dependencies_cmd = ['pip install bleak', 'pip install requests']
        if wof_data['system_type'] == "nt": # Windows Auto Install
            library.ascii_art("Hmm, I've detected that you are running under Windows!")
            print(f"[!] Wall of Flippers >> Would it be okay if we ran these commands on your system?\n{json.dumps(windows_dependencies_cmd, indent=4)}")
            user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
            if user_input_ok.lower() == "y":
                print(f"[!] Wall of Flippers >> What pip version do you use >> (pip/pip3)")
                user_input_pip = input("[?] Wall of Flippers (pip/pip3) >> ")
                windows_dependencies_cmd = [cmd.replace("pip", user_input_pip) for cmd in windows_dependencies_cmd]
                print(f"[!] Wall of Flippers >> Installing dependencies...")
                for cmd in windows_dependencies_cmd:
                    os.system(cmd)
                library.ascii_art("We have successfully installed the dependencies!")
                print(f"[!] Wall of Flippers >> Dependencies installed successfully!")
        if wof_data['system_type'] == "posix": # Linux Auto Install
            library.ascii_art("Hmm, I've detected that you are running under linux!")
            print(f"[!] Wall of Flippers >> Would it be okay if we ran these commands on your system?\n{json.dumps(linux_dependencies_cmd, indent=4)}")
            user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
            if user_input_ok.lower() == "y":
                print(f"[!] Wall of Flippers >> What pip version do you use >> (pip/pip3)")
                user_input_pip = input("[?] Wall of Flippers (pip/pip3) >> ")
                linux_dependencies_cmd = [cmd.replace("pip", user_input_pip) for cmd in linux_dependencies_cmd]
                print(f"[!] Wall of Flippers >> Add '--break-system-packages' to the {user_input_pip} command if you are using a virtual environment? (Y/N)")
                user_input_pip = input("[?] Wall of Flippers (Y/N) >> ")
                if user_input_pip.lower() == "y":
                    linux_dependencies_cmd = [cmd + " --break-system-packages" if "pip" and not "apt-get install" in cmd else cmd for cmd in linux_dependencies_cmd]
                print(f"[!] Wall of Flippers >> Installing dependencies...")
                for cmd in linux_dependencies_cmd:
                    os.system(cmd)
                library.ascii_art("We have successfully installed the dependencies!")
                print("[!] Wall of Flippers >> Dependencies installed successfully!")
    except KeyboardInterrupt:
        library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        exit()
