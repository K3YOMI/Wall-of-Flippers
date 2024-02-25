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


# Standard library Imports
import os
import sys
import shutil
import time
import asyncio
import json
import random
import argparse






# Wall of Flippers Imports
import utils.wof_cache as cache # for important configurations and data :3
import utils.wof_library as library # for important functions :3
import utils.wof_display as wall_display # for important functions :3
import utils.wof_install as installer # for important functions and classes :3

Scanner = None # This is the scanner object for the bluepy package (Default = None)


def sort_packets(ble_packets:list):
    """Sorts the BLE packets based on the type of packet"""
    any_flippers_discovered = False
    flippers_discovered_list = []
    latest_discovered_list = []
    forbidden_packets_list = cache.wof_data['forbidden_packets']

    for advertisement in ble_packets:
        advertisement_name = advertisement['Name']
        advertisement_type = advertisement['Type']
        advertisement_rssi = advertisement['RSSI']
        advertisement_mac = advertisement['MAC']
        advertisement_packets = advertisement['PCK']
        advertisement_uuid = advertisement['UUID']
        advertisement_blacklist_check = None
        for advertisement_packet in advertisement_packets:
            for forbidden_packet in forbidden_packets_list:
                if all(p1 == p2 or p2 == "_" for p1, p2 in zip(advertisement_packet, forbidden_packet['PCK'])):
                    int_get_non_underscore = len(forbidden_packet['PCK'].replace("_", ""))
                    int_total_found = sum(p != "_" for p in advertisement_packet)
                    if int_total_found >= int_get_non_underscore:
                        cache.wof_data['forbidden_packets_found'].append({
                            "Type": forbidden_packet['TYPE'],
                            "PCK": advertisement_packet,
                            "MAC": advertisement_mac,
                        })
                if len(advertisement_packet) > cache.wof_data['min_byte_length']: # If the packet is longer than the minimum byte length, then it is a valid packet we want to log
                    cache.wof_data['all_packets_found'].append({
                        "PCK": advertisement_packet,
                        "MAC": advertisement_mac,
                    })
        if advertisement_name.lower().startswith("flipper"):
            int_recorded = int(time.time())
            cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if advertisement_mac != flipper['MAC']]
            t_data = {
                "Name": advertisement_name,
                "RSSI": advertisement_rssi,
                "MAC": advertisement_mac,
                "Detection Type": "Name",
                "unixLastSeen": int_recorded,
                "unixFirstSeen": int_recorded,
                "Type": advertisement_type,
                "UUID": advertisement_uuid,
            }
            if advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                cache.wof_data['found_flippers'].append(t_data)
                cache.wof_data['live_flippers'].append(t_data)
                library.log(t_data)
                any_flippers_discovered = True
                flippers_discovered_list.append(t_data)
                latest_discovered_list = t_data
        elif any(advertisement_mac.startswith(addr) for addr in ("80:e1:26", "80:e1:27")): # Credit to @elliotwutingfeng (https://github.com/elliotwutingfeng) for this fix
            int_recorded = int(time.time())
            cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if advertisement_mac != flipper['MAC']]
            t_data = {
                "Name": advertisement_name,
                "RSSI": advertisement_rssi,
                "MAC": advertisement_mac,
                "Detection Type": "Address",
                "unixLastSeen": int_recorded,
                "unixFirstSeen": int_recorded,
                "Type": advertisement_type,
                "UUID": advertisement_uuid,
            }
            if advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                cache.wof_data['found_flippers'].append(t_data)
                cache.wof_data['live_flippers'].append(t_data)
                library.log(t_data)
                any_flippers_discovered = True
                flippers_discovered_list.append(t_data)
                latest_discovered_list = t_data
        elif advertisement_uuid != "NOT FOUND":
            int_recorded = int(time.time())
            cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if advertisement_mac != flipper['MAC']]
            t_data = {
                "Name": advertisement_name,
                "RSSI": advertisement_rssi,
                "MAC": advertisement_mac,
                "Detection Type": "Identifier",
                "unixLastSeen": int_recorded,
                "unixFirstSeen": int_recorded,
                "UUID": advertisement_uuid,
                "Type": advertisement_type
            }
            if advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                cache.wof_data['found_flippers'].append(t_data)
                cache.wof_data['live_flippers'].append(t_data)
                library.log(t_data)
                any_flippers_discovered = True
                flippers_discovered_list.append(t_data)
                latest_discovered_list = t_data
    if not any_flippers_discovered:
        wall_display.display(None)
        cache.wof_data['bool_isScanning'] = False
    else:
        latest_name = latest_discovered_list['Name']
        latest_mac = latest_discovered_list['MAC']
        wall_display.display(f"I've found a wild {latest_name} ({latest_mac})")
        cache.wof_data['bool_isScanning'] = False   
async def detection_async(os_param:str, detection_type=0): # renamed 'os' and 'type' to avoid conflict with built-in functions. Feel free to change it to something more appropriate as I'm not exactly sure what they do
    """BLE detection"""
    try:
        cache.wof_data['bool_isScanning'] = True
        ble_packets = []
        if os_param == "nt": # Windows Detection
            devices = await BleakScanner.discover()
            if devices:
                for device in devices:
                    advertisement_name = str(device.name)
                    advertisement_addr = str(device.address.lower())
                    advertisement_rssi = str(device.rssi)
                    advertisment_data = device.metadata.get('manufacturer_data')
                    advertisement_uuid = str(device.metadata.get('uuids'))
                    device_uuid = "NOT FOUND"
                    device_type = "NOT FOUND"
                    if (advertisement_uuid == "['00003082-0000-1000-8000-00805f9b34fb']"): # White Flipper
                        device_type = "White"
                        device_uuid = advertisement_uuid
                    if (advertisement_uuid == "['00003081-0000-1000-8000-00805f9b34fb']"): # Black Flipper
                        device_type = "Black"
                        device_uuid = advertisement_uuid
                    if (advertisement_uuid == "['00003083-0000-1000-8000-00805f9b34fb']"): # Transparent Flipper
                        device_uuid = "Transparent"
                        device_uuid = advertisement_uuid
                    ble_packets.append({
                        "Name": advertisement_name,
                        "MAC": advertisement_addr,
                        "RSSI": advertisement_rssi,
                        "PCK": "NOT FOUND",
                        "UUID": device_uuid,
                        "Manufacturer": "NOT FOUND",
                        "Type": device_type
                    })
            else:
                cache.wof_data['bool_isScanning'] = False
        elif os_param == "posix": # Linux Detection
            scanner = Scanner(detection_type) # Thank you Talking Sasquach for testing this!
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
                cache.wof_data['bool_isScanning'] = False
        else: # Unsupported OS
            print("[!] Wall of Flippers >> Error: Type not supported")
            cache.wof_data['bool_isScanning'] = False
        sort_packets(ble_packets)
    except Exception as e:
        library.print_ascii_art("Error: Failed to scan for BLE devices")
        print("[!] Wall of Flippers >> Error: Failed to scan for BLE devices >> " + str(e))
        sys.exit()

# Start of the program
library.check_json_file_exist()
os.system('cls' if os.name == 'nt' else 'clear')

cache.wof_data['system_type'] = os.name
if cache.wof_data['system_type'] == "posix": # Linux Auto Install
    if not os.path.exists(".venv/bin/activate"): # Check if the user has setup their virtual environment
        library.print_ascii_art("Uh oh, it seems like you have not setup your virtual environment yet!")
        print("[!] Wall of Flippers >> It seems like you have not setup your virtual environment yet.\n\t      Reason: .venv/bin/activate does not exist.\n[!] Wall of Flippers >> Would you like to setup your virtual environment now?")
        if input("[?] Wall of Flippers (Y/N) >> ").lower() == "y":
            os.system("python3 -m venv .venv")
            print("[!] Wall of Flippers >> Virtual environment setup successfully!")
            sys.exit()
    if library.is_in_venv() == False: # Check if the user is in their virtual environment
        library.print_ascii_art("Uh oh, it seems like you are not in your virtual environment!")
        print("[!] Wall of Flippers >> It seems like you are not in your virtual environment. Please use the following command to enter your virtual environment.\n\tsource .venv/bin/activate\n\tor\n\tbash wof.sh")
        sys.exit()


parser = argparse.ArgumentParser(description='Wall of Flippers', prog='WallofFlippers.py')
parser.add_argument('-w', '--wall', action='store_true', help='Wall of Flippers')
parser.add_argument('-i', '--install', action='store_true', help='Install Wall of Flippers')
parser.add_argument('-d', '--device', action='store', help='Select a bluetooth device')

args = parser.parse_args()



if args == None:
    selection_box = library.init()
else:
    if args.wall:
        selection_box = 'wall_of_flippers'
    elif args.install:
        selection_box = 'install_dependencies'
    else:
        selection_box = library.init()
if selection_box == 'wall_of_flippers':
    try:
        if cache.wof_data['system_type'] == "nt":
            from bleak import BleakScanner  # Windows BLE Package
        if cache.wof_data['system_type'] == "posix":
            from bluepy.btle import Scanner 
    except ImportError as e:
        library.print_ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {e}")
        sys.exit()
    if cache.wof_data['system_type'] == "posix" and not os.geteuid() == 0:
        library.print_ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        sys.exit()
    try:
        ble_adapters = []
        if cache.wof_data['system_type'] == "posix":
            ble_adapters = [adapter for adapter in os.listdir('/sys/class/bluetooth/') if 'hci' in adapter]
            # make a selection of the bluetooth adapter
            if args.device == None:
                print("\n\n[#]\t[HCI DEVICE]\n" + "-" * shutil.get_terminal_size().columns)
                for adapter in ble_adapters:
                    print(f"{ble_adapters.index(adapter)}".ljust(8) + f"{adapter}".ljust(34))
                DEVIC_HCI = input("[?] Wall of Flippers >> ")
            else:
                DEVIC_HCI = args.device
        else:
            DEVIC_HCI = 0
        wall_display.display("Thank you for using Wall of Flippers")
        while True:
            if not cache.wof_data['bool_isScanning']:
                asyncio.run(detection_async(cache.wof_data['system_type'],DEVIC_HCI))
            time.sleep(1)
    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        sys.exit()
if selection_box == 'install_dependencies':
    installer.init()
