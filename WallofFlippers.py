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
 



# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # Wall of Flippers "cache" for important configurations and data :3
import utils.wof_library as library # Wall of Flippers "library" for important functions and classes :3
import utils.wof_display as wall_display # Wall of Flippers "display" for important functions and classes :3
import utils.wof_install as installer # Wall of Flippers "install" for important functions and classes :3
import utils.wof_bleexploitation as ble_exploitation # Wall of Flippers "ble_exploitation" for important functions and classes :3



# Basic Imports
import os
import time
import asyncio
import json
import random



Scanner = None # This is the scanner object for the bluepy package (Default = None)



def sort_packets(ble_packets): # This is the function for sorting the BLE packets
    bool_flipper_discovered = False
    table_flippers_discovered = []
    table_latest_discovered = []
    bool_ctf = library.in_ctf()
    table_forbidden_packets_list = cache.wof_data['forbidden_packets']
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
                                cache.wof_data['forbidden_packets_found'].append({
                                    "Type": packet['TYPE'],
                                    "PCK": indiv_packet,
                                    "MAC": Advertisement_mac,
                                })
                        if len(indiv_packet) > cache.wof_data['min_byte_length']: # If the packet is longer than the minimum byte length, then it is a valid packet we want to log
                            cache.wof_data['all_packets_found'].append({
                                "PCK": indiv_packet,
                                "MAC": Advertisement_mac,
                            })
        if Advertisement_name.lower().startswith("flipper"):
            int_recorded = int(time.time())
            cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
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
            if Advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                cache.wof_data['found_flippers'].append(t_data)
                cache.wof_data['live_flippers'].append(t_data["MAC"])
                library.log(t_data)
                bool_flipper_discovered = True
                table_flippers_discovered.append(t_data)
                table_latest_discovered = t_data
        elif any(Advertisement_mac.startswith(addr) for addr in ("80:e1:26", "80:e1:27")): # Credit to @elliotwutingfeng (https://github.com/elliotwutingfeng) for this fix
                int_recorded = int(time.time())
                cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
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
                if Advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                    cache.wof_data['found_flippers'].append(t_data)
                    cache.wof_data['live_flippers'].append(t_data["MAC"])
                    library.log(t_data)
                    bool_flipper_discovered = True
                    table_flippers_discovered.append(t_data)
                    table_latest_discovered = t_data
        elif Advertisement_uuid != "NOT FOUND":
                int_recorded = int(time.time())
                cache.wof_data['found_flippers'] = [flipper for flipper in cache.wof_data['found_flippers'] if Advertisement_mac != flipper['MAC']]
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
                if Advertisement_mac not in [flipper['MAC'] for flipper in cache.wof_data['found_flippers']]:
                    cache.wof_data['found_flippers'].append(t_data)
                    cache.wof_data['live_flippers'].append(t_data["MAC"])
                    library.log(t_data)
                    bool_flipper_discovered = True
                    table_flippers_discovered.append(t_data)
                    table_latest_discovered = t_data
    if not bool_ctf:
        if not bool_flipper_discovered:
            wall_display.display(None)
        else:
            latest_name = table_latest_discovered['Name']
            latest_mac = table_latest_discovered['MAC']
            wall_display.display(f"I've found a wild {latest_name} ({latest_mac})")
    elif bool_ctf:
        if len(table_flippers_discovered) > 0:
            bool_alreadylogged = False 
            for flippers in cache.table_ctf_compeition_confiugrations['temp_collection']:
                if flippers == table_flippers_discovered[0]['MAC']:
                    bool_alreadylogged = True
            if not bool_alreadylogged:
                cache.table_ctf_compeition_confiugrations['temp_collection'].append(table_flippers_discovered[0]['MAC'])
                http_header = {
                    "username": cache.table_ctf_compeition_confiugrations['ctf_username'],
                    "secret-key": cache.table_ctf_compeition_confiugrations['ctf_key'],
                    "password": cache.table_ctf_compeition_confiugrations['ctf_password'],
                    "flippers": json.dumps(table_flippers_discovered)
                }
                try:
                    http = requests.post(f"{cache.table_ctf_compeition_confiugrations['ctf_link']}/send-flipper-data", headers=http_header) # This can be exploited on so many levels, but I'll find a better way ehhehe (Just a simple demo)
                except Exception as error:
                    print(f"[!] Wall of Flippers >> Failed to send flipper data to the CTF Host >> Possibly Offline??\nError: {error}")
    else: # If the system type is not supported, display an error message
        print("[!] Wall of Flippers >> Error: Type not supported")
    cache.wof_data['bool_isScanning'] = False




async def detection_async(os, type=0): # This is the async function for the BLE detection
    try:
        cache.wof_data['bool_isScanning'] = True
        ble_packets = []
        if os == "nt": # Windows Detection
            devices = await BleakScanner.discover()
            if devices:
                for device in devices:
                    Advertisement_name = str(device.name)
                    Advertisement_addr = str(device.address.lower())
                    Advertisement_rssi = str(device.rssi)
                    Advertisment_Data = device.metadata.get('manufacturer_data')
                    Advertisement_uuid = str(device.metadata.get('uuids'))
                    device_uuid = "NOT FOUND"
                    device_type = "NOT FOUND"
                    if (Advertisement_uuid == "['00003082-0000-1000-8000-00805f9b34fb']"): # White Flipper
                        device_type = "White"
                        device_uuid = Advertisement_uuid
                    if (Advertisement_uuid == "['00003081-0000-1000-8000-00805f9b34fb']"): # Black Flipper
                        device_type = "Black"
                        device_uuid = Advertisement_uuid
                    if (Advertisement_uuid == "['00003083-0000-1000-8000-00805f9b34fb']"): # Transparent Flipper
                        device_uuid = "Transparent"
                        device_uuid = Advertisement_uuid
                    ble_packets.append({
                        "Name": Advertisement_name,
                        "MAC": Advertisement_addr,
                        "RSSI": Advertisement_rssi,
                        "PCK": "NOT FOUND",
                        "UUID": device_uuid,
                        "Manufacturer": "NOT FOUND",
                        "Type": device_type
                    })
            else:
                cache.wof_data['bool_isScanning'] = False
        elif os == "posix": # Linux Detection
            scanner = Scanner(type) # Thank you Talking Sasquach for testing this!
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
    except Exception as error:
        library.ascii_art("Error: Failed to scan for BLE devices")
        print("[!] Wall of Flippers >> Error: Failed to scan for BLE devices >> " + str(error))
        exit()






os.system("clear || cls")
cache.wof_data['system_type'] = os.name
if cache.wof_data['system_type'] == "posix": # Linux Auto Install
    if not os.path.exists(".venv/bin/activate"): # Check if the user has setup their virtual environment
        library.ascii_art("Uh oh, it seems like you have not setup your virtual environment yet!")
        print("[!] Wall of Flippers >> It seems like you have not setup your virtual environment yet.\n\t      Reason: .venv/bin/activate does not exist.")
        print("[!] Wall of Flippers >> Would you like to setup your virtual environment now?")
        user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
        if user_input_ok.lower() == "y":
            os.system("python3 -m venv .venv")
            print("[!] Wall of Flippers >> Virtual environment setup successfully!")
            exit()
    if library.in_venv() == False: # Check if the user is in their virtual environment
        library.ascii_art("Uh oh, it seems like you are not in your virtual environment!")
        print("[!] Wall of Flippers >> It seems like you are not in your virtual environment. Please use the following command to enter your virtual environment.")
        print("\tsource .venv/bin/activate")
        print("\tor")
        print("\tbash wof.sh")
        exit()
selection_box = library.init()
if selection_box == "wall_of_flippers" or selection_box == "capture_the_flippers":
    try:
        import requests
        if cache.wof_data['system_type'] == "nt":
            from bleak import BleakScanner  # Windows BLE Package
        if cache.wof_data['system_type'] == "posix":
            from bluepy.btle import Scanner 
    except Exception as error:
        library.ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {error}")
        exit()
if selection_box == 'wall_of_flippers':
    print("[!] Wall of Flippers >> Starting Wall of Flippers")
    if cache.wof_data['system_type'] == "posix" and not os.geteuid() == 0:
        library.ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        exit()  # Check if the user is root (Linux)
    try:
        ble_adapters = []
        if cache.wof_data['system_type'] == "posix":
            ble_adapters = [adapter for adapter in os.listdir('/sys/class/bluetooth/') if 'hci' in adapter]
            # make a selection of the bluetooth adapter
            print("\n\n[#]\t[HCI DEVICE]")
            print("-------------------------------------------------------------------------------------------------")
            for adapter in ble_adapters:
                print(f"{ble_adapters.index(adapter)}".ljust(8) + f"{adapter}".ljust(34))
            device_hci = input("[?] Wall of Flippers >> ")
        else:
            device_hci = 0
        wall_display.display("Thank you for using Wall of Flippers")
        while True:
            if not cache.wof_data['bool_isScanning']:
                asyncio.run(detection_async(cache.wof_data['system_type'],device_hci))
            time.sleep(1)
    except KeyboardInterrupt:
        library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        exit()
if selection_box == 'capture_the_flippers':
    import utils.wof_capture as wall_capture # Wall of Flippers "capture" for important functions and classes :3
    if cache.wof_data['system_type'] == "posix" and os.geteuid() != 0:
        library.ascii_art("I require root privileges to run!")
        print("[!] Wall of Flippers >> I require root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        exit()  # Check if the user is root (Linux)
    cache.table_ctf_compeition_confiugrations['is_enabled'] = True
    url = cache.table_ctf_compeition_confiugrations['ctf_link']
    password = cache.table_ctf_compeition_confiugrations['ctf_password']
    key = cache.table_ctf_compeition_confiugrations['ctf_key']
    username = cache.table_ctf_compeition_confiugrations['ctf_username']
    dialogue_options = cache.wof_data['ctf_directory_options']
    library.ascii_art("Please select an option to continue")
    print(f"\n\n[#]\t[ACTION]\t\t\t  [DESCRIPTION]")
    print("-------------------------------------------------------------------------------------------------")
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
                        ble_adapters = []
                        if cache.wof_data['system_type'] == "posix":
                            ble_adapters = [adapter for adapter in os.listdir('/sys/class/bluetooth/') if 'hci' in adapter]
                            # make a selection of the bluetooth adapter
                            print("\n\n[#]\t[HCI DEVICE]")
                            print("-------------------------------------------------------------------------------------------------")
                            for adapter in ble_adapters:
                                print(f"{ble_adapters.index(adapter)}".ljust(8) + f"{adapter}".ljust(34))
                            device_hci = input("[?] Wall of Flippers >> ")
                        else:
                            device_hci = 0
                        try: 
                            while True:
                                if not cache.wof_data['bool_isScanning']:
                                    wall_capture.display("You have successfully connected to the host - Good luck!")
                                    asyncio.run(detection_async(cache.wof_data['system_type'],device_hci))
                                time.sleep(1)  # Don't worry about this - Everything is fine... :P
                        except KeyboardInterrupt:
                            library.ascii_art("Thank you for using Wall of Flippers... Goodbye!")
                            print("\n[!] Wall of Flippers >> Exiting...")
                            exit()
                except Exception as error:
                    print(
                        f"[!] Capture the Flippers >> Error: Failed to connect to the CTF Host >> Login Failed\nError: {error}")
if selection_box == 'advertise_bluetooth_packets':
    ble_exploitation.init()
if selection_box == 'install_dependencies':
    installer.init()
