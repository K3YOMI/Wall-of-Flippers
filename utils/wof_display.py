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

# 



# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # Wall of Flippers "cache" for important configurations and data :3
import utils.wof_library as library # Wall of Flippers "library" for important functions and classes :3



# Basic Imports
import json

def display(str_text):
    # Load flipper data from Flipper.json
    with open('Flipper.json', 'r') as flipper_file:
        flipper_data = json.load(flipper_file)
    # Update base_flippers list with flipper data
    cache.wof_data['base_flippers'] = [key for key in flipper_data]
    # Categorize flipper data into live and offline flippers
    for key in cache.wof_data['base_flippers']:
        key['Name'] = key['Name'].replace("Flipper ", "")[:15]
        if 'Type' not in key:  # Add a check for the 'Type' key
            key['Type'] = "Unknown"
        if key['MAC'] in cache.wof_data['live_flippers']:
            cache.wof_data['display_live'].append(key)
        else:
            cache.wof_data['display_offline'].append(key)
    # Calculate various statistics
    t_allignment = 8
    ble_spamming_macs = []
    int_total_blacklisted_packets = len(cache.wof_data['forbidden_packets_found'])
    int_total_ble_packets = len(cache.wof_data['all_packets_found'])
    int_online_flippers = len(cache.wof_data['display_live'])
    int_offline_flippers = len(cache.wof_data['display_offline'])
    # Display ASCII art
    if str_text == None or str_text == "":
        library.ascii_art(None)
    else:
        library.ascii_art(str_text)
    # Display statistics for POSIX systems
    if cache.wof_data['system_type'] == "posix":
        print(f"Latest Forbidden Advertisements..: {int_total_blacklisted_packets}")
        print(f"Latest Advertisements............: {int_total_ble_packets}")
        if len(cache.wof_data['all_packets_found']) > 0:
            packet_counts = {}
            addrs = []
            # Count occurrences of each packet
            for packet in cache.wof_data['all_packets_found']:
                pck_value = packet['PCK']
                packet_counts[pck_value] = packet_counts.get(pck_value, 0) + 1
            # Find the most common packet
            most_common_packet = max(packet_counts, key=packet_counts.get)
            # Find unique addresses for the most common packet
            for packet in cache.wof_data['all_packets_found']:
                if packet['PCK'] == most_common_packet:
                    if packet['MAC'] not in addrs:
                        addrs.append(packet['MAC'])
                if len(packet['PCK']) > cache.wof_data['max_byte_length']:
                    cache.wof_data['forbidden_packets_found'].append({"MAC": packet['MAC'], "PCK": packet['PCK'], "Type": f"SUSPICIOUS_PACKET (+{cache.wof_data['max_byte_length']} bytes)"})
            print(f"Most Common Advertisement........: {most_common_packet} ({packet_counts[most_common_packet]} packets) ({len(addrs)} unique addresses)")
            # Add a summary if there are too many unique addresses
            if len(addrs) > 5:
                cache.wof_data['forbidden_packets_found'].append({"MAC": str(len(addrs)) + " Unique Addresses", "PCK": most_common_packet, "Type": "SUSPICIOUS_ADVERTISEMENT"})
        else: 
            print(f"Most Common Advertisement........: None")
        # Display forbidden packets
        if len(cache.wof_data['forbidden_packets_found']) > 0:
            t_packets = 0
            print("\n\n[!] Wall of Flippers >> These packets may not be related to the Flipper Zero.\n")
            print(f"[NAME]\t\t\t\t\t[ADDR]\t\t   [PACKET]")
            print("-----------------------------------------------------------------------------------------------") 
            for key in cache.wof_data['forbidden_packets_found']:
                if ble_spamming_macs.count(key['MAC']) == 0:
                    ble_spamming_macs.append(key['MAC'])
                    t_packets += 1 
                    if t_packets <= cache.wof_data['max_ble_packets']: # Max amount of packets to display on the screen
                        print(f"{key['Type'].ljust(t_allignment)}\t\t{key['MAC'].ljust(t_allignment)}  {key['PCK'].ljust(t_allignment)}")
            if int_total_blacklisted_packets > cache.wof_data['ble_threshold']:
                print(f"------------------ Bluetooth Low Energy (BLE) Attacks Detected ({int_total_blacklisted_packets} Advertisements) --------------------")
    else:
        print(f"\n------------------  BLE Attack Detection is not available for Windows yet. ------------------")
    # Display flipper statistics
    print(f"\nTotal Online.....................: {int_online_flippers}")
    print(f"Total Offline....................: {int_offline_flippers}")
    print(f"\n\n[FLIPPER]{''.ljust(t_allignment)}[ADDR]{''.ljust(t_allignment)}\t\t[FIRST]{''.ljust(t_allignment)}[LAST]\t{''.ljust(t_allignment)}[RSSI]{''.ljust(t_allignment)}\t[Detection]{''.ljust(t_allignment)}")
    print("----------------------------------------------------------------------------------------------------")
    # Display online flippers
    if int_online_flippers > 0:
        t_live = 0
        print("(ONLINE DEVICES)".center(100))
        cache.wof_data['display_live'] = sorted(cache.wof_data['display_live'], key=lambda k: k['unixLastSeen'], reverse=True)
        for key in cache.wof_data['display_live']:
            t_live += 1
            if t_live <= cache.wof_data['max_online']:
                key['RSSI'] = str(f"{key['RSSI']} dBm")
                print(f"{key['Name'].ljust(t_allignment)}\t{key['MAC'].ljust(t_allignment)}\t{library.unix2text(key['unixFirstSeen']).ljust(t_allignment)}\t{library.unix2text(key['unixLastSeen']).ljust(t_allignment)}\t{str(key['RSSI']).ljust(t_allignment)}\t{key['Detection Type']} ({key['Type']})".ljust(t_allignment))         
            if t_live > cache.wof_data['max_online']:
                t_left_over = int_online_flippers - cache.wof_data['max_online']
                print(f"Too many <online> devices to display. ({t_left_over} devices)".center(100))
                break 
    # Display offline flippers
    if int_offline_flippers > 0:
        t_offline = 0
        print("(OFFLINE DEVICES)".center(100))
        cache.wof_data['display_offline'] = sorted(cache.wof_data['display_offline'], key=lambda k: k['unixLastSeen'], reverse=True)
        for key in cache.wof_data['display_offline']:
            t_offline += 1
            if t_offline <= cache.wof_data['max_offline']:
                key['RSSI'] = str(f"{key['RSSI']} dBm")  
                print(f"{key['Name'].ljust(t_allignment)}\t{key['MAC'].ljust(t_allignment)}\t{library.unix2text(key['unixFirstSeen']).ljust(t_allignment)}\t{library.unix2text(key['unixLastSeen']).ljust(t_allignment)}\t{str(key['RSSI']).ljust(t_allignment)}\t{key['Detection Type']} ({key['Type']})".ljust(t_allignment))                    
                if t_offline > cache.wof_data['max_offline']:
                    t_left_over = int_offline_flippers - cache.wof_data['max_offline']
                    print(f"Too many <offline> devices to display. ({t_left_over} devices)".center(100))
                    break
    # Display message if no devices detected
    if int_offline_flippers == 0 and int_online_flippers == 0:
        print("No devices detected".center(100))
    # Reset data for next display
    cache.wof_data['display_live'] = []
    cache.wof_data['display_offline'] = []
    cache.wof_data['live_flippers'] = []
    cache.wof_data['forbidden_packets_found'] = []
    cache.wof_data['all_packets_found'] = []
    cache.wof_data['duplicated_packets'] = []
    cache.wof_data['base_flippers'] = []