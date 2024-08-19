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
import utils.wof_blechat as blechat # for important functions and classes :3

Scanner = None # This is the scanner object for the bluepy package (Default = None)


parser = argparse.ArgumentParser(description='Wall of Flippers', prog='WallofFlippers.py')
parser.add_argument('-w', '--wall', action='store_true', help='Wall of Flippers')
parser.add_argument('-i', '--install', action='store_true', help='Install Wall of Flippers')
parser.add_argument('-d', '--device', action='store', help='Select a bluetooth device')
parser.add_argument('-b', '--badgemode', action='store_true', help='Toggle Badge Mode')
parser.add_argument('-a', '--advertise', action='store_true', help='Advertise WoF Exsistance (OFF=Default)')
args = parser.parse_args()

async def detection_async(os_param:str, detection_type=0):
    try:
        cache.wof_data['bool_isScanning'] = True
        ble_packets = []
        if (os_param != "nt") and (os_param != "posix"): 
            library.print_ascii_art("Error: Unsupported OS")
            print("[!] Wall of Flippers >> Error: Unsupported OS")
            sys.exit()
        if os_param == "nt": # Windows Detection
            devices = await BleakScanner.discover()
            if devices: # If devices are found
                for device in devices:
                    device_info = library.flipper2Validation(device, os_param)
                    ble_packets.append(device_info)
        if os_param == "posix": # Linux Detection
            scanner = Scanner(detection_type) # Thank you Talking Sasquach for testing this!
            devices = scanner.scan(5) # Scan the area for 5 seconds....
            ble_packets = []
            if devices: # If devices are found
                for device in devices:
                    device_info = library.flipper2Validation(device, os_param)
                    ble_packets.append(device_info)
        any_flippers_discovered, flippers_discovered_list, latest_discovered_list = library.ble2Sort(ble_packets)
        if not any_flippers_discovered:
            wall_display.display(None)
            cache.wof_data['bool_isScanning'] = False
        else:
            latest_name = latest_discovered_list['Name']
            latest_mac = latest_discovered_list['MAC']
            wall_display.display(f"I've found a wild {latest_name} ({latest_mac})")
            cache.wof_data['bool_isScanning'] = False
    except Exception as e:
        library.print_ascii_art("Error: Failed to scan for BLE devices")
        print("[!] Wall of Flippers >> Error: Failed to scan for BLE devices >> " + str(e))
        cache.wof_data['bool_isScanning'] = False

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


if args == None:
    selection_box = library.init()
else:
    if args.badgemode:
        cache.wof_data['badge_mode'] = not cache.wof_data['badge_mode']
    if args.advertise:
        cache.wof_data['toggle_adveriser'] = not cache.wof_data['toggle_adveriser'] 
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
            if (cache.wof_data['toggle_adveriser']):
                from utils.bluetooth_utils import toggle_device, start_le_advertising, stop_le_advertising
                import bluetooth._bluetooth as bluez
    except ImportError as e:
        library.print_ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {e}")
        sys.exit()
    if cache.wof_data['system_type'] == "posix" and not os.geteuid() == 0:
        library.print_ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        sys.exit()
    try:
        DEVIC_HCI = library.adapter2Selection(args.device)
        if (cache.wof_data['toggle_adveriser']) and (cache.wof_data['system_type'] == "posix"): # Start the BLE Advertiser if the user has it enabled
            sock = bluez.hci_open_dev(int(DEVIC_HCI))
            toggle_device(int(DEVIC_HCI), True)
        wall_display.display(f"Thank you for using Wall of Flippers!")
        while True:
            time.sleep(1)
            if (cache.wof_data['toggle_adveriser']) and (cache.wof_data['system_type'] == "posix"): # Start the BLE Advertiser if the user has it enabled
                for i in range (0, 10):
                    advertisementData = cache.wof_data['wof_advertiser']
                    advertismentName = tuple(cache.wof_data['wof_advertiserName'] .encode()) # Convert the advertiser name to bytes
                    advertisementData += advertismentName
                    advertisementData += (0x00,) * (31 - len(advertisementData)) # Padding
                    if len(advertisementData) > 31:
                        print("[!] Wall of Flippers >> Error: Advertisement data is too long; change the wof_advertiserName in utils/wof_cache.py")
                        sys.exit()
                    to_hex = lambda data: ''.join(f"{i:02x}" for i in advertisementData)
                    data_hex = to_hex(advertisementData)
                    start_le_advertising(sock, adv_type=0x03, data=advertisementData)
                    time.sleep(0.1)
                    stop_le_advertising(sock)
            if not cache.wof_data['bool_isScanning']:
                asyncio.run(detection_async(cache.wof_data['system_type'], DEVIC_HCI))
    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        sys.exit()
if selection_box == 'install_dependencies':
    installer.init()
if selection_box == 'wall_of_talking':
    if cache.wof_data['system_type'] == "posix" and not os.geteuid() == 0:
        library.print_ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        sys.exit()
    if cache.wof_data['system_type'] != "posix":
        library.print_ascii_art("Error: BLE Chat is not supported on this OS")
        print("[!] Wall of Flippers >> Error: BLE Chat is not supported on this OS")
        sys.exit()
    blechat.init()
