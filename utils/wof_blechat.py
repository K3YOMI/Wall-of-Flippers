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
import platform
import os
import sys
import time
import json
import asyncio
import shutil
import threading


# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # Wall of Flippers "cache" for important configurations and data :3
import utils.wof_library as library # Wall of Flippers "library" for important functions and classes :3

def chect2Limit(string:str, limit:int):
    if len(string) > limit:
        print(f"[!] Wall of Flippers >> {string} is too long! Please enter a name with {limit} characters or less.")
        return False
    return True

def send_traffic(sock:int, start:object, stop:object):
    try: 
        displayName = cache.wof_data['wof_displayName'] + "::" # :: = Splitter
        totalCharsLeft = 31 - len(displayName) - len(cache.wof_data['wof_bleAdvertiserRaw'])
        global customMessage
        library.print_ascii_art("You are now broadcasting your messages!")
        for i in cache.wof_data['cachedMessages'][:20]:
            readable_date = time.strftime('%H:%M:%S', time.localtime(i['time']))
            print(f"[+] {readable_date} {i['displayName']} >> {i['message']}")
        customMessage = input(f"[?] Wall of Flippers >> (MAX: {totalCharsLeft} chars) (Empty = Refresh) >> ")
        if (customMessage == ""): send_traffic(sock, start, stop)
        isStringAllowed = chect2Limit(customMessage, totalCharsLeft)
        if (not isStringAllowed): library.print_ascii_art(f"Message is too long! Please enter a message with less than {totalCharsLeft} characters."); send_traffic(sock, start, stop)
        cache.wof_data['cachedMessages'].append({"displayName": cache.wof_data['wof_displayName'], "message": customMessage, "time": int(time.time())})
        for i in range(0, 10):
            advertisementData = cache.wof_data['wof_blechatAdvertiser']
            advertisementData = list(advertisementData)
            advertisementData += list(bytes.fromhex(displayName.encode().hex())) 
            advertisementData += list(bytes.fromhex(customMessage.encode().hex()))
            advertisementData = tuple(advertisementData)
            advertisementData += (0x00,) * (31 - len(advertisementData))
            to_hex = lambda data: ''.join(f"{i:02x}" for i in advertisementData)
            start(sock, adv_type=0x03, data=advertisementData)
            time.sleep(0.1)
            stop(sock)     
        send_traffic(sock, start, stop) 
    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        stop(sock)
        sys.exit()


def sort_traffic(ble_packets:list):
    for advertisement in ble_packets:
        advertisement_packets = advertisement['PCK']
        for advertisement_packet in advertisement_packets:
            if str(advertisement_packet).startswith(cache.wof_data['wof_bleAdvertiserRaw']):
                decodedMessage = bytes.fromhex(advertisement_packet.replace(cache.wof_data['wof_bleAdvertiserRaw'], "")).decode('utf-8').replace("\x00", "")
                decodedDisplayName = decodedMessage.split("::")[0]
                decodedDisplayMessage = decodedMessage.split("::")[1]
                # check for duplicates
                if any(i['message'] == decodedDisplayMessage for i in cache.wof_data['cachedMessages']) and any(i['displayName'] == decodedDisplayName for i in cache.wof_data['cachedMessages']):
                    continue
                cache.wof_data['cachedMessages'].append({"displayName": decodedDisplayName, "message": decodedDisplayMessage, "time": int(time.time())})
async def read_traffic(sock:int, Scanner:object):
    cache.wof_data['bool_isScanning'] = True
    ble_packets = []
    scanner = Scanner(sock) # Thank you Talking Sasquach for testing this!
    devices = scanner.scan(5) # Scan the area for 5 seconds....
    if devices:
        for device in devices:
            scan_list = device.getScanData()
            device_packets = []
            device_formatted = []
            for scan_list_item in scan_list:
                device_formatted.append({"ADTYPE": scan_list_item[0], "Description": scan_list_item[1], "Value": scan_list_item[2]})
            for i_data in device_formatted:
                device_packets.append(i_data['Value'])
            ble_packets.append({"PCK": device_packets})
    sort_traffic(ble_packets)
    cache.wof_data['bool_isScanning'] = False


def init():
    try: 
        from utils.bluetooth_utils import toggle_device, start_le_advertising, stop_le_advertising
        import bluetooth._bluetooth as bluez
        from bluepy.btle import Scanner
    except ImportError as e:
        library.print_ascii_art("Error: Failed to import dependencies")
        print(f"[!] Wall of Flippers >> Failed to import dependencies >> {e}")
        sys.exit()
    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        sys.exit()
    DEVIC_HCI = library.adapter2Selection()
    sock = bluez.hci_open_dev(int(DEVIC_HCI))
    toggle_device(int(DEVIC_HCI), True)
    displayNameSelection = input("[?] Wall of Flippers >> Please enter your display name (MAX: 6 chars) >> ")
    isStringAllowed = chect2Limit(displayNameSelection, 6)
    if (not isStringAllowed): sys.exit()
    cache.wof_data['wof_displayName'] = displayNameSelection
    try:
        threading.Thread(target=send_traffic, args=(sock, start_le_advertising, stop_le_advertising)).start()
        while True:
            time.sleep(0.1)
            if not cache.wof_data['bool_isScanning']:
                asyncio.run(read_traffic(DEVIC_HCI, Scanner))
    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        stop_le_advertising(sock)
        sys.exit()
