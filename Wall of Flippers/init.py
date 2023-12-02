art_ascii = """
                      YAao,
                        Y8888b,
                      ,oA8888888b,
                ,aaad8888888888888888bo,
             ,d888888888888888888888888888b,
           ,888888888888888888888888888888888b,             
          d8888888888888888888888888888888888888,           
         d888888888888888888888888888888888888888b
        d888888P'                    `Y88888888Ꙩ \,
        88888P'                    Ybaaaa888888  Ꙩ l
       a8888'                      `Y8888P' `V888888            (k3yomi && jbohack)
     d8888888a                                `Y8888             
    AY/'' `\Y8b                                 ``Y8b
    Y'      `YP                                    ~~
     _       __      ____         ____   _________                           
    | |     / /___ _/ / /  ____  / __/  / ____/ (_)___  ____  ___  __________
    | | /| / / __ `/ / /  / __ \/ /_   / /_  / / / __ \/ __ \/ _ \/ ___/ ___/
    | |/ |/ / /_/ / / /  / /_/ / __/  / __/ / / / /_/ / /_/ /  __/ /  (__  ) 
    |__/|__/\__,_/_/_/   \____/_/    /_/   /_/_/ .___/ .___/\___/_/  /____/  
                                              /_/   /_/                               
    Last Updated >> 2023-08-15
"""


## Imports and Shit ##

import os, time, random, json
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle


## Values and Arrays of Hell ##
arr_discoveredFlippers = []
arr_baseFlippers = []
arr_displayLive = []
arr_displayOffline = []

int_backupInterval = 120 # 120 Second Interval for Saving the backup file...
int_maxLive = 30 # Max Online Devices to show 
int_maxOffline = 10 # Max Offline Devices to show
int_currentUnix = int(time.time())
class Utilities:
    def warn(str_message):
        print(f"[!] WoF >> {str_message}")
    def linux():
        if os.name != "posix":
            Utilities.warn("This is currently only being supported on Linux.")
            exit()
        else:
            return True
    def root():
        if os.geteuid() != 0:
            Utilities.warn("This program requires root privileges.")
            exit()
        else:
            return True
    def unixconverter(int_unix):
        int_cur = int(time.time())
        int_diff = int_cur - int_unix
        minutes = int_diff / 60
        seconds = int_diff % 60
        return f"{int(minutes)}m {int(seconds)}s"


class FliperZeroDetection:
    def createBackup(): ## Creates a (int_currentUnix) interval to save the Flippers.json in case of corruption..
        int_currentUnix = int(time.time())
        createFile = open(f"Saved-Devices/SaveID-{str(int_currentUnix)}.json", "w")
        openFile = open(f"Flipper.json", "r", encoding="utf-8")
        load = json.load(openFile)
        json.dump(load, createFile, indent=4)
    def logFlipper(str_name, arr_data): # logs the device and saves information to the Flippers.json file
        openFile = open(f"Flipper.json", "r", encoding="utf-8")
        load = json.load(openFile)
        for flipper in load:
            if flipper['macAddr'] == arr_data['macAddr']:
                flipper['lastSeen'] = arr_data['lastSeen']
                flipper['decibelMiliwats'] = arr_data['decibelMiliwats']
                flipper['detectionType'] = arr_data['detectionType']
                with open('Flipper.json', 'w') as output:
                    json.dump(load, output, indent=4)
                openFile.close()
                return
        load.append(arr_data)
        with open('Flipper.json', 'w') as output:
            json.dump(load, output, indent=4)
        openFile.close()
    def loggedFlippers(): # Returns the logged flippers from the Flippers.json file
        openFile = open(f"Flipper.json", "r", encoding="utf-8")
        load = json.load(openFile)
        for flipper in load:
            arr_baseFlippers.append(flipper)
        openFile.close()
    def fancydisplay(): # Displays the flippers in a fancy way
        ## Glob ##
        global arr_discoveredFlippers
        global arr_baseFlippers
        global arr_displayLive
        global arr_displayOffline

        # Start Displaying Fun Stuff #
        FliperZeroDetection.loggedFlippers()
        int_allignment = 10
        for flipper in arr_baseFlippers:
            if len(flipper['Name']) > 15:
                flipper['Name'] = flipper['Name'][:15]
            if flipper['macAddr'] in arr_discoveredFlippers:
                arr_displayLive.append(flipper)
            else:
                arr_displayOffline.append(flipper)
        int_totalLive = 0
        int_totalOffline = 0
        os.system("clear || cls")
        print(art_ascii)
        print(f"Total Online >> {len(arr_displayLive)}")
        print(f"Total Offline >> {len(arr_displayOffline)}\n\n")
        print(f"[NAME]\t\t[MAC]\t\t   [F. TIME]  [L. TIME]  [dBm]    [TYPE]     [SPOOF]   [LIVE]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if (len(arr_displayLive) > 0):
            print(f"( ONLINE DEVICES )".center(95))
            for flipper in arr_displayLive:
                int_totalLive += 1
                if int_totalLive < int_maxLive:
                    print(
                        flipper['Name'].ljust(int_allignment) + "\t" +
                        flipper['macAddr'].ljust(int_allignment) + "  " +
                        Utilities.unixconverter(flipper['firstSeen']).ljust(int_allignment) + " " +
                        Utilities.unixconverter(flipper['lastSeen']).ljust(int_allignment) + " " +
                        str(flipper['decibelMiliwats']).ljust(int_allignment) + "" +
                        flipper['detectionType'].ljust(int_allignment) + "" +
                        str(flipper['isSpoofing']).ljust(int_allignment) + "" +
                        "LIVE"
                    )
                if int_totalLive == int_maxLive - 1:
                    str_live = len(arr_displayLive) - int_maxLive
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <online> devices to display. ({str_live} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        if (len(arr_displayOffline) > 0):
            arr_displayOffline = sorted(arr_displayOffline, key=lambda k: k['lastSeen'], reverse=True)

            print(f"( OFFLINE DEVICES )".center(95))
            for flipper in arr_displayOffline:
                int_totalOffline += 1
                if int_totalOffline < int_maxOffline:
                    print(
                        flipper['Name'].ljust(int_allignment) + "\t" +
                        flipper['macAddr'].ljust(int_allignment) + "  " +
                        Utilities.unixconverter(flipper['firstSeen']).ljust(int_allignment) + " " +
                        Utilities.unixconverter(flipper['lastSeen']).ljust(int_allignment) + " " +
                        str(flipper['decibelMiliwats']).ljust(int_allignment) + "" +
                        flipper['detectionType'].ljust(int_allignment) + "" +
                        str(flipper['isSpoofing']).ljust(int_allignment) + "" +
                        "OFFLINE"
                    )
                if int_totalOffline == int_maxOffline - 1:
                    str_offline = len(arr_displayOffline) - int_maxOffline
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <offline> devices to display. ({str_offline} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        arr_displayLive = []
        arr_displayOffline = []
        arr_baseFlippers = []
    def scan(): # Scans for BLE devices and logs them
        try:
            if Utilities.linux() == True and Utilities.root() == True:
                scan_now = Scanner() 
                scan_dev = scan_now.scan(0.5)
                for device in scan_dev:
                    for (adtype, desc, value) in device.getScanData():
                        dump = json.dumps(device.getScanData())
                        if (desc == "Complete Local Name"):
                            if "Flipper" in value:
                                recorded_time = int(time.time())
                                flipper_name = value
                                flipper_mac = device.addr
                                flipper_dbm = device.rssi
                                if not "80:e1:26" and "80:e1:27" in device.addr:
                                    arr_temp = {
                                        "Name": flipper_name,
                                        "macAddr":  str(flipper_mac),
                                        "firstSeen": recorded_time,
                                        "lastSeen": recorded_time,
                                        "decibelMiliwats": str(flipper_dbm) + " dBm",
                                        "detectionType": "BLE",
                                        "isSpoofing": "TRUE"
                                    }
                                else:
                                    arr_temp = {
                                        "Name": flipper_name,
                                        "macAddr": str(flipper_mac),
                                        "firstSeen": recorded_time,
                                        "lastSeen": recorded_time,
                                        "decibelMiliwats": str(flipper_dbm) + " dBm",
                                        "detectionType": "BLE",
                                        "isSpoofing": "FALSE"
                                    }
                                arr_discoveredFlippers.append(flipper_mac)
                                FliperZeroDetection.logFlipper(flipper_name, arr_temp)
                            elif "80:e1:26" or "80:e1:27" in device.addr:
                                recorded_time = int(time.time())
                                flipper_name = value
                                flipper_mac = device.addr
                                flipper_dbm = device.rssi
                             
                                arr_temp = {
                                    "Name": flipper_name,
                                    "macAddr": str(flipper_mac),
                                    "firstSeen": recorded_time,
                                    "lastSeen": recorded_time,
                                    "decibelMiliwats": str(flipper_dbm) + " dBm",
                                    "detectionType": "BLE",
                                    "isSpoofing": "TRUE"
                                }
                                arr_discoveredFlippers.append(flipper_mac)
                                FliperZeroDetection.logFlipper(flipper_name, arr_temp)
                return "Err, something went wrong with validation"
        except (RuntimeError, TypeError, NameError, ValueError) as err:
            Utilities.warn(f"Error >> {err}")
            exit()
if __name__ == '__main__':
    os.system("clear || cls")
    print(art_ascii)
    if Utilities.linux() == True and Utilities.root() == True:
        while True:
            arr_baseFlippers = []
            arr_liveFlippers = []
            arr_discoveredFlippers = []
            FliperZeroDetection.scan()
            FliperZeroDetection.fancydisplay()
            unix = int(time.time())
            if unix - int_currentUnix > int_backupInterval:
                FliperZeroDetection.createBackup()
                int_currentUnix = unix
            time.sleep(1)

                



