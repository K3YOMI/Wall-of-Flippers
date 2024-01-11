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
import shutil
import json
import requests


# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # Wall of Flippers "cache" for important configurations and data :3
import utils.wof_library as library # Wall of Flippers "library" for important functions and classes :3


def display(str_text):
    """Display the leaderboard and user's stats"""
    library.print_ascii_art("You have successfully connected to the host - Good luck!")
    leaderboard_data = []
    total_flippers_found = 0
    headers = {
        "username": cache.table_ctf_compeition_confiugrations['ctf_username'],
        "secret-key": cache.table_ctf_compeition_confiugrations['ctf_key'], 
        "password": cache.table_ctf_compeition_confiugrations['ctf_password']
    }
    try:
        # Get leaderboard data from the CTF host
        http = requests.get(f"{cache.table_ctf_compeition_confiugrations['ctf_link']}/leaderboard", headers=headers) 
        if http.status_code == 200:
            response = http.json()
            total_flippers_found = response['total_flippers']
            cache.table_ctf_compeition_confiugrations['my_collection'] = response['my_flippers']
            response['leaderboard'] = sorted(response['leaderboard'], key=lambda k: k['score'], reverse=True)
            players_top_10 = 0
            for player in response['leaderboard']:
                players_top_10 += 1
                if players_top_10 >= 10: break
                leaderboard_data.append({"name": player['username'], "score": player['score'], "flippers": player['flippers']})
            # Display global and personal flipper stats
            print(f"\nGlobal Captured: {total_flippers_found}")
            print(f"My Flippers Captuted: {len(cache.table_ctf_compeition_confiugrations['my_collection'])}")
            print("TOP 10 LEADERBOARD\n".center(95))
            print("[RANK]\t[USERNAME]\t[CURRENT SCORE]\t[FLIPPERS CAPTURED]")
            print("---------------------------------------------------------------------------------------------------")
            for player in leaderboard_data:
                if len(player['name']) > 10:
                    player['name'] = player['name'][:10] + "..."
                print(f"{(str(leaderboard_data.index(player)+1)).ljust(8)}{player['name'].ljust(8)}\t{player['score']}\t\t{player['flippers']}")     
            print("\n\n")
            print("YOUR STATS\n".center(95))
            print(f"[FLIPPER]{''.ljust(7)}[ADDR]{''.ljust(8)}\t\t[Detection]{''.ljust(8)}")
            print("---------------------------------------------------------------------------------------------------")
            for key in cache.table_ctf_compeition_confiugrations['my_collection']:
                key['flippers'] = json.loads(key['flippers'])
                if len(key['flippers']) > 0: # If there are more than 2 flippers, then the user has captured a flipper
                    for flipper in key['flippers']:
                        flipper = flipper[0]
                        flipper['Name'] = flipper['Name'].replace("Flipper ", "")
                        if len(flipper['Name']) > 15:
                            flipper['Name'] = flipper['Name'][:15]
                        print(f"{flipper['Name'].ljust(8)}\t{flipper['MAC'].ljust(8)}\t{flipper['Detection Type']} ({flipper['Type']})".ljust(8))
                else:
                    print("You have not captured any flippers yet.".center(shutil.get_terminal_size().columns))
    except Exception as e:
        print(f"[!] Wall of Flippers >> Failed to connect to the CTF Host >> Possibly Offline??\nError: {e}")
