#!/usr/bin/python3

#                               YAao,                            
#                                 Y8888b,                        Created By: Kiyomi & Jbohack
#                               ,oA8888888b,                     Kiyomi: https://ko-fi.com/k3yomi
#                         ,aaad8888888888888888bo,               Jbohack: https://ko-fi.com/jbohack
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

# Standard library Imports
import os
import sys
import shutil
import random
import time
import json


# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # for important configurations and data :3


def log(s_table:dict): # Logs data to the log file (utils/wof_log.txt)
    """logs data to the log file (utils/wof_log.txt)"""
    with open('db/Flipper.json', 'r', encoding='utf-8') as flipper_file: # Load flipper data from Flipper.json with UTF-8 encoding
        flipper_data = json.load(flipper_file)
    for s_flipper in flipper_data:
        if s_flipper["MAC"] == s_table["MAC"] and s_flipper["Name"] == s_table["Name"]:
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
            "UID": s_table['UID'],
        })
    with open('db/Flipper.json', 'w', encoding='utf-8') as flipper_file: # Save the flipper data to Flipper.json
        json.dump(flipper_data, flipper_file, indent=4)   

def required2files():
    """Checks for the required files which are Flipper.json and Backup.json, some really poor implementation but it works."""
    if not os.path.isdir("db"): os.mkdir("db")
    if not os.path.isfile("db/Flipper.json"):
        with open("db/Flipper.json", "w") as new_file:
            json.dump([], new_file)
    if not os.path.isfile("db/Backup.json"):
        with open("db/Backup.json", "w") as new_file:
            json.dump([], new_file)  
    

def unix2text(unix_timestamp:int):
    """converts a unix timestamp to a human readable format."""
    current_timestamp = int(time.time())
    t_different = current_timestamp - unix_timestamp
    t_minutes, t_seconds = divmod(t_different, 60)
    if t_minutes > 1000:
        t_hours, t_minutes = divmod(t_minutes, 60)
        if t_hours > 24:
            t_days, t_hours = divmod(t_hours, 24)
            if t_days > 1000:
                t_years, t_days = divmod(t_days, 365)
                return f"1Year+"
            return f"{t_days}d {t_hours}h"
        return f"{t_hours}h {t_minutes}m"
    return f"{t_minutes}m {t_seconds}s"

def ble2Sort(packets:list): # Sorts BLE packets and updates the list/cache
    """Sorts the BLE packets based on the type of packet"""
    any_flippers_discovered = False
    flippers_discovered_list = []
    latest_discovered_list = []
    suspiciousFlippers = []
    forbidden_packets_list = cache.wof_data['forbidden_packets']
    wof_advertiserRaw = cache.wof_data['wof_advertiserRaw']
    totalFlippersFound = (advertisement[0]["flipper"] for advertisement in packets)
    totalNewFound = 0
    totalNewFound = sum(1 for advertisement in packets if advertisement[0]["flipper"] and not any(flipper['MAC'] == advertisement[0]["address"] for flipper in cache.wof_data['base_flippers']))
    totalNewFoundArray = [advertisement[0] for advertisement in packets if advertisement[0]["flipper"] and not any(flipper['MAC'] == advertisement[0]["address"] for flipper in cache.wof_data['base_flippers'])]
    for advertisement in totalNewFoundArray: suspiciousFlippers.append(advertisement["address"])
    if (totalNewFound >= cache.wof_data['max_flippers_ratelimited'] and not cache.wof_data['is_ratelimited']):
        cache.wof_data['is_ratelimited'] = True 
        cache.wof_data['last_ratelimit'] = int(time.time()) + cache.wof_data['ratelimit_seconds']
    for advertisement in packets:
        advertisement = advertisement[0]
        adv_name = advertisement["name"]
        adv_type = advertisement["color"]
        adv_rssi = advertisement["rssi"]
        adv_address = advertisement["address"]
        adv_packets = advertisement["packets"]
        adv_uid = advertisement["uid"]
        adv_isFlipper = advertisement["flipper"]
        adv_detection = advertisement["detection"]
        adv_blacklisted = None
        if adv_address in suspiciousFlippers and cache.wof_data['is_ratelimited']: adv_isFlipper = False # If the flipper is in the suspicious list, mark it down as not a flipper
        for packet in adv_packets:
            for forbidden_packet in forbidden_packets_list:
                if all(p1 == p2 or p2 == "_" for p1, p2 in zip(packet, forbidden_packet['PCK'])):
                    int_get_non_underscore = len(forbidden_packet['PCK'].replace("_", ""))
                    int_total_found = sum(p != "_" for p in packet)
                    if int_total_found >= int_get_non_underscore:
                        cache.wof_data['forbidden_packets_found'].append({"Type": forbidden_packet['TYPE'],"PCK": packet,"MAC": adv_address, "RSSI": adv_rssi})
                if len(packet) > cache.wof_data['min_byte_length']: # If the packet is longer than the minimum byte length, then it is a valid packet we want to log
                    cache.wof_data['all_packets_found'].append({"PCK": packet,"MAC": adv_address})
            if str(packet).startswith(wof_advertiserRaw):
                decodedAdvertiser = bytes.fromhex(packet.replace(wof_advertiserRaw, "")).decode('utf-8').replace("\x00", "")
                cache.wof_data['nearbyWof'].append(decodedAdvertiser)
        if adv_isFlipper: # if flipper is set to true :3
            int_recorded = int(time.time())
            cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if adv_address != flipper['MAC']] 
            t_data = {"Name": adv_name,"RSSI": adv_rssi,"MAC": adv_address,"Detection Type": adv_detection,"unixLastSeen": int_recorded,"unixFirstSeen": int_recorded,"Type": adv_type,"UID": adv_uid}
            if not any(flipper['MAC'] == adv_address and flipper['Name'] == adv_name for flipper in cache.wof_data['found_flippers']): # if the flipper is not in the list, add it
                cache.wof_data['found_flippers'].append(t_data)
                cache.wof_data['live_flippers'].append(t_data)
                log(t_data)
                any_flippers_discovered = True
                flippers_discovered_list.append(t_data)
                latest_discovered_list = t_data
    if (cache.wof_data['last_ratelimit'] < int(time.time())) and cache.wof_data['is_ratelimited']:
        cache.wof_data['is_ratelimited'] = False
    return any_flippers_discovered, flippers_discovered_list, latest_discovered_list, totalNewFound, cache.wof_data['is_ratelimited']

def flipper2Validation(data:list, os:str): # Validates incoming flippers/ble packets
    device_packets = []
    device_information = []
    device_name = "UNK"
    device_manufacturer = "UNK"
    device_uid = "UNK"
    device_color = "UNK"
    device_formatted = []
    device_mac = "UNK"
    device_rssi = data.rssi
    isFlipper = False
    keyFound = False
    detectionType = "Unknown"
    if os == "nt":
        device_mac = str(data.address.lower())
        device_name = str(data.name)
        advertisement_uid = str(data.metadata.get('uids')).replace("['", "").replace("']", "")
        for key, value in cache.wof_data['flipper_types'].items():
            if key in advertisement_uid:
                device_uid = advertisement_uid
                device_color = value
                device_packets = ["06", device_name, device_uid, "00"]
                keyFound = True
        if not keyFound:
            if advertisement_uid.startswith("0000308") and advertisement_uid.endswith("0000-1000-8000-00805f9b34fb"):
                device_uid = advertisement_uid
                device_color = "SPF"
                device_packets = ["06", device_name, device_uid, "00"]
    if os == "posix":
        device_mac = data.addr.lower()
        scan_list = data.getScanData()
        for scan_list_item in scan_list: 
            device_formatted.append({"ADTYPE": scan_list_item[0], "Description": scan_list_item[1], "Value": scan_list_item[2]})
        for i_data in device_formatted:
            if i_data['Description'] == "Complete Local Name":
                device_name = i_data['Value']
            if i_data['Description'] == "Manufacturer":
                device_manufacturer = i_data['Value']
            for key, value in cache.wof_data['flipper_types'].items():
                if i_data['Value'] == key:
                    device_uid = i_data['Value']
                    device_color = value
                    keyFound = True
            if not keyFound:
                if i_data['Value'].startswith("0000308") and i_data['Value'].endswith("0000-1000-8000-00805f9b34fb"):
                    device_uid = i_data['Value']
                    device_color = "SPF"
            device_packets.append(i_data['Value'])
    if device_uid != "UNK" and len(device_packets) == 4:
        if device_packets[0] == "06" and device_packets[1] == device_name and device_packets[2] == device_uid and device_packets[3] == "00":
            if device_name.lower().startswith("flipper"):
                isFlipper = True
                detectionType = "Name"
            elif device_mac.startswith(("80:e1:26", "80:e1:27", "0c:fa:22")): # FLIPPER DEVICES INC (https://maclookup.app/macaddress/0cfa22)
                detectionType = "Address"
                isFlipper = True
            else:
                detectionType = "Identifier"
                isFlipper = True
    device_information.append({
        "name": device_name,
        "address": device_mac,
        "rssi": device_rssi,
        "packets": device_packets,
        "uid": device_uid,
        "manufacturer": device_manufacturer,
        "color": device_color,
        "genericdata": device_formatted,
        "detection": detectionType,
        "flipper": isFlipper
    })
    return device_information

def adapter2Selection(deviceArgs:str=None):
    ble_adapters = []
    if cache.wof_data['system_type'] == "posix":
        ble_adapters = [adapter for adapter in os.listdir('/sys/class/bluetooth/') if 'hci' in adapter]
        # make a selection of the bluetooth adapter
        if deviceArgs == None:
            print("\n\n[#]\t[HCI DEVICE]\n" + "-" * shutil.get_terminal_size().columns)
            for adapter in ble_adapters:
                print(f"{ble_adapters.index(adapter)}".ljust(8) + f"{adapter}".ljust(34))
            DEVIC_HCI = input("[?] Wall of Flippers >> ")
        else:
            DEVIC_HCI = deviceArgs
    else:
        DEVIC_HCI = 0
    if DEVIC_HCI == "": # If the user does not select a device, default to 0
        DEVIC_HCI = 0
    return DEVIC_HCI

def is_in_venv():
    """Returns True if the user is in a virtual environment, otherwise returns False"""
    return sys.prefix != sys.base_prefix

def print_ascii_art(custom_text:str=None):
    """Displays ASCII art in the terminal with the custom text if provided, otherwise displays a random quote"""
    os.system('cls' if os.name == 'nt' else 'clear')
    r_quote = random.choice(cache.wof_data['dolphin_thinking']) if not custom_text else custom_text
    # selecting adequate ASCII art based on the terminal size and if the user is in narrow mode
    print("\033[0;94m")
    if cache.wof_data['narrow_mode']:
        print(f"{cache.wof_data['ascii_small']}\n\"{r_quote}\"\n".center(50) + "\033[0m")
    else:
        ascii_art = cache.wof_data['ascii_normal']

        if cache.wof_data['badge_mode']:
           # shorten ascii art by 10 lines
            ascii_art = "\n".join(ascii_art.split("\n")[:-7])
            print(f"{ascii_art.replace('[RANDOM_QUOTE]', r_quote)}\n\033[0m")
        else:
            print(f"{ascii_art.replace('[RANDOM_QUOTE]', r_quote)}\n\033[0m")

def init():
    """Initial Selection Box (Upon starup)
    This init() function allows the user to select what action they would like to preform (cached options stored in utils/wof_cache.py)
    returns: the action the user selected (str)
    """
    # check terminal size to set narrow mode (false by default)
    if shutil.get_terminal_size().columns < cache.wof_data['narrow_mode_limit']: # if the terminal size is less than *narrow_mode_limit* columns (default: 100)
        cache.wof_data['narrow_mode'] = True

    dialogue_options = cache.wof_data['init_directory_options']
    dialogue_options_dict = {option['option']: option['return'] for option in dialogue_options}
    print_ascii_art("Please Select an option to continue")

    #Library dependencies check
    #This checks the bleak, bluepy, and bluetooth python packages and libraries
    #for Wall of Flippers to work properly.

    try:
        import bleak # Universal (Mostly for Windows) BLE Library
        print("[X] Bleak is installed")
    except ImportError:
        print("[ ] Bleak is installed")
    try:
        import bluepy # Linux BLE Library
        print("[X] Bluepy is installed")
    except ImportError:
        print("[ ] Bluepy is installed")
    try:
        import bluetooth # Bluetooth Library
        print("[X] Bluetooth is installed")
    except ImportError:
        print("[ ] Bluetooth is installed")


    #Initial selection box for the user to select what they want to do.
        
    if cache.wof_data['narrow_mode']:
        # dont display the description if the terminal is too narrow
        print("\n\n[#]\t[ACTION]\n" + "-"*shutil.get_terminal_size().columns + "\n" + "\n".join([f"{option['option'].ljust(8)}{option['action']}" for option in dialogue_options]))
    else:
        print("\n\n[#]\t[ACTION]\t\t\t  [DESCRIPTION]\n" + "-"*shutil.get_terminal_size().columns + "\n" + "\n".join([f"{option['option'].ljust(8)}{option['action'].ljust(34)}{option['description']}" for option in dialogue_options]))


    try:
        str_input = input("\n[?] Wall of Flippers >> ")
        return dialogue_options_dict.get(str_input)
    except KeyboardInterrupt:
        print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        sys.exit()