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

# Basic Imports
import os 
import sys
import random 
import time 
import json



def log(s_table): # This function logs data to the log file (utils/wof_log.txt)
    with open('Flipper.json', 'r') as flipper_file: # Load flipper data from Flipper.json
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
            "UUID": s_table['UUID'],
        })
    with open('Flipper.json', 'w') as flipper_file: # Save the flipper data to Flipper.json
        json.dump(flipper_data, flipper_file, indent=4)     

def unix2text(s_raw): # This function converts a unix timestamp to a human readable format.
    current_timestamp = int(time.time())
    t_different = current_timestamp - s_raw
    t_minutes, t_seconds = divmod(t_different, 60)
    if t_minutes > 1000:
        t_minutes = ">999"
    return f"{t_minutes}m {t_seconds}s"

def in_ctf(): # Returns True if the user is in Capture The Flippers mode, otherwise returns False
    return cache.table_ctf_compeition_confiugrations['is_enabled'] 

def in_venv(): # Returns True if the user is in a virtual environment, otherwise returns False
    return sys.prefix != sys.base_prefix 

def ascii_art(str_text): # ASCII Art Function - This function is used to display ASCII art in the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    s_ascii_art = cache.wof_data['ascii']
    if in_ctf(): # If the user is in Capture The Flippers mode, then display the Capture The Flippers ASCII art
        s_ascii_art = cache.wof_data['ascii_ctf']
    r_quote = random.choice(cache.wof_data['dolphin_thinking']) if not str_text else str_text
    print(s_ascii_art.replace("[RANDOM_QUOTE]", r_quote))

def init(): # Initial Selection Box (Upon starup) - This init() function allows the user to select what action they would like to preform (cached options stored in utils/wof_cache.py)  
    dialogue_options = cache.wof_data['init_directory_options']
    dialogue_options_dict = {option['option']: option['return'] for option in dialogue_options}
    ascii_art(f"Please Select an option to continue")

    #Library dependencies check
    #This checks the bleak, bluepy, requests, and bluetooth python packages and libraries
    #for Wall of Flippers to work properly.

    try:
        import bleak # Universal (Mostly for Windows) BLE Library
        print(f"[X] Bleak is installed")
    except:
        print(f"[ ] Bleak is not installed")
    try:
        import bluepy # Linux BLE Library
        print(f"[X] Bluepy is installed")
    except:
        print(f"[ ] Bluepy is not installed")
    try:
        import requests # HTTP Library
        print(f"[X] Requests is installed")
    except:
        print(f"[ ] Requests is not installed")
    try:
        import bluetooth # Bluetooth Library
        print(f"[X] Bluetooth is installed")
    except:
        print(f"[ ] Bluetooth is not installed")


    #Initial selection box for the user to select what they want to do.
    #Capture The Flippers, Wall of Flippers, etc....

    print("\n\n[#]\t[ACTION]\t\t\t  [DESCRIPTION]")
    print("-------------------------------------------------------------------------------------------------")
    print("\n".join([f"{option['option'].ljust(8)}{option['action'].ljust(34)}{option['description']}" for option in dialogue_options]))
    try:
        str_input = input(f"\n[?] Wall of Flippers >> ")
        return dialogue_options_dict.get(str_input) 
    except KeyboardInterrupt:
        ascii_art(f"Thank you for using Wall of Flippers... Goodbye!")
        print(f"\n[!] Wall of Flippers >> Exiting...")
        exit()
    

