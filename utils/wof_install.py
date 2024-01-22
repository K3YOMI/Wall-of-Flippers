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
import platform
import os
import sys
import json

# Wall of Flippers "library" for important functions and classes :3
import utils.wof_cache as cache # Wall of Flippers "cache" for important configurations and data :3
import utils.wof_library as library # Wall of Flippers "library" for important functions and classes :3


def init():
    try: # while there is no KeyboardInterrupt
        library.print_ascii_art("Welcome to the easy install process! Please read carefully.")

        linux_cmd = ["python3 -m pip install distro"]
        debian_dependencies_cmd = ['sudo apt-get install libglib2.0-dev', 'python3 -m pip install bluepy', 'python3 -m pip install requests', 'python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez']
        fedora_dependencies_cmd = ['sudo dnf install glib2-devel', 'python3 -m pip install bluepy', 'python3 -m pip install requests', 'python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez']
        windows_dependencies_cmd = ['pip install bleak', 'pip install requests']
        system_type = os.name

        # Windows Auto Install
        if system_type == "nt":
            library.print_ascii_art("Hmm, I've detected that you are running under Windows!")
            print(f"[!] Wall of Flippers >> Would it be okay if we ran these commands on your system?\n{json.dumps(windows_dependencies_cmd, indent=4)}")

            user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
            if user_input_ok.lower() == "y":
                print("[!] Wall of Flippers >> What pip version do you use >> (pip/pip3)")
                user_input_pip = input("[?] Wall of Flippers (pip/pip3) >> ")
                windows_dependencies_cmd = [cmd.replace("pip", user_input_pip) for cmd in windows_dependencies_cmd]
                print("[!] Wall of Flippers >> Installing dependencies...")
                for cmd in windows_dependencies_cmd:
                    os.system(cmd)
                library.print_ascii_art("We have successfully installed the dependencies!") # todo: add a check to see if the dependencies were really installed successfully
                print("[!] Wall of Flippers >> Dependencies installed successfully!")

        # Linux Auto Install
        elif system_type == "posix":
            library.print_ascii_art("Hmm, I've detected that you are running under linux!")
            linux_distro = [
                {"name": "debian", "rolling": ["debian", "ubuntu", "kali", "raspbian"]},
                {"name": "fedora", "rolling": ["fedora"]},
                {"name": "arch", "rolling": ["arch"]}
            ]
            def get_like_distro():
                os_file = open("/etc/os-release", "r")
                os_data = os_file.read()
                os_file.close()
                os_data = os_data.split("\n")
                os_data = [data.split("=") for data in os_data]
                os_data = {data[0]: data[1].replace('"', "") for data in os_data if len(data) == 2}
                for distro in linux_distro:
                    name_only = os_data["NAME"].lower().split(" ")[0]
                    if os_data["NAME"].lower() in distro["rolling"]:
                        return [distro["name"], distro['rolling']]
                return [os_data["NAME"], os_data["NAME"]]
            distribution_info = get_like_distro()
            # Fedora Auto Install
            if "fedora" in distribution_info[0]:
                library.print_ascii_art("Hmm, I've detected that you are running under Fedora!")
                print(f"[!] Wall of Flippers >> Would it be okay if we ran these commands on your system?\n{json.dumps(fedora_dependencies_cmd, indent=4)}")
                user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
                if user_input_ok.lower() == "y":
                    print("[!] Wall of Flippers >> Installing dependencies...")
                    for cmd in fedora_dependencies_cmd:
                        os.system(cmd)
                    library.print_ascii_art("We have successfully installed the dependencies!") # todo: add a check to see if the dependencies were really installed successfully
                    print("[!] Wall of Flippers >> Dependencies installed successfully!")
            
            # Debian Auto Install
            elif "debian" in distribution_info[0]:
                library.print_ascii_art("Hmm, I've detected that you are running under Debian!")
                print(f"[!] Wall of Flippers >> Would it be okay if we ran these commands on your system?\n{json.dumps(debian_dependencies_cmd, indent=4)}")
                user_input_ok = input("[?] Wall of Flippers (Y/N) >> ")
                if user_input_ok.lower() == "y":
                    print("[!] Wall of Flippers >> Installing dependencies...")
                    for cmd in debian_dependencies_cmd:
                        os.system(cmd)
                    library.print_ascii_art("We have successfully installed the dependencies!") # todo: add a check to see if the dependencies were really installed successfully
                    print("[!] Wall of Flippers >> Dependencies installed successfully!")
            else:
                library.print_ascii_art(f"Hmm, I am unable to provide an automated install for your system. ({distribution_info[0]})")
                print(f"[!] Wall of Flippers >> Please install the dependencies manually. ({distribution_info[0]})")

    except KeyboardInterrupt:
        library.print_ascii_art("Thank you for using Wall of Flippers... Goodbye!")
        print("\n[!] Wall of Flippers >> Exiting...")
        sys.exit()
