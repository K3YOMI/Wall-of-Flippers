
# All rights reserved to the contributors of the bluepy library. I am not the owner of this library. However, I am the owner of the code below handling
# the bluetooth scanning detection for the Flipper zero device. For any questions / mistakes, please feel free to contact me on my github account @K3YOMI
# Have a blessed day!


#   What is WallofFlippers? 
#       Wall of Flippers is designed to capture bluetooth devices in the range of your device. In addition, it will detect the Flipper Zero device and 
#       display it on the screen. It will also log the Flipper Zero device in a JSON file for future reference and other devices as well.


#  How to use?
#       1. Install bluepy (pip3 install bluepy) 
#       2. Run the script (python3/python/py noflip.py)
#       3. Watch it scan for all the bluetooth capable devices in range of your device.
#       4. If you see a Flipper Zero device, it will be detected and you will be notified. shortly after with a timestamp, MAC, RSSI, and name.


# Made with Love... uWu

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
       a8888'                      `Y8888P' `V888888            (https://github.com/K3YOMI && https://github.com/jbohack)
     d8888888a                                `Y8888                               * Made With Love *
    AY/'' `\Y8b                                 ``Y8b
    Y'      `YP                                    ~~

    $$\      $$\           $$\ $$\                  $$$$$$\        $$$$$$$$\ $$\ $$\                                                   
    $$ | $\  $$ |          $$ |$$ |                $$  __$$\       $$  _____|$$ |\__|                                                  
    $$ |$$$\ $$ | $$$$$$\  $$ |$$ |       $$$$$$\  $$ /  \__|      $$ |      $$ |$$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ 
    $$ $$ $$\$$ | \____$$\ $$ |$$ |      $$  __$$\ $$$$\           $$$$$\    $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
    $$$$  _$$$$ | $$$$$$$ |$$ |$$ |      $$ /  $$ |$$  _|          $$  __|   $$ |$$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|\$$$$$$\  
    $$$  / \$$$ |$$  __$$ |$$ |$$ |      $$ |  $$ |$$ |            $$ |      $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |       \____$$\ 
    $$  /   \$$ |\$$$$$$$ |$$ |$$ |      \$$$$$$  |$$ |            $$ |      $$ |$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      $$$$$$$  |
    \__/     \__| \_______|\__|\__|       \______/ \__|            \__|      \__|\__|$$  ____/ $$  ____/  \_______|\__|      \_______/ 
                                                                                    $$ |      $$ |                                    
                                                                                    $$ |      $$ |                                    
                                                                                    \__|      \__|                                    
"""



import os,time,random
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle
import json


found_flippers = []
data_baseFlippers = []
live_flippers = []
bool_detectNonFlippers = False


class FlipDetection:
    def __logFlipper__(name, data): 
        db = open('Flipper.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
             if flipper['MAC'] == data['MAC']:
                flipper['Time Last Seen'] = data['Time Last Seen']
                flipper['RSSI'] = data['RSSI']
                flipper['Detection Type'] = data['Detection Type']
                with open('Flipper.json', 'w') as f:
                    json.dump(file_data, f, indent=4)
                db.close()
                return
        file_data.append(data)
        with open('Flipper.json', 'w') as f:
               json.dump(file_data, f, indent=4)
        db.close()
    def __getLoggedFlippers__():
        db = open('Flipper.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
            data_baseFlippers.append(flipper)
        db.close()
    def __hexString__(hexValue):
        return ''.join([chr(int(''.join(c), 16)) for c in zip(hexValue[0::2], hexValue[1::2])])
    def __warn__(msg):
        print('[!] NoFlip >> ' + msg)
    def __inLinux__():
        if os.name != 'posix':
            FlipDetection.__warn__("Unfortunately, this script should only be ran on linux, mac, or unix based systems. Thank you. (You could remove this restriction if you want to.)")
            exit()
        else:
            return True
    def __inRoot__():
        if os.geteuid() != 0:
            FlipDetection.__warn__("Unfortunately, this script should only be ran as root. Scanning for bluetooth devices requires root permissions. Thank you.")
            exit()
        else:
            return True
    def __detectFlipperBoo__(alt):
        if bool_detectNonFlippers == True:
            return True
        if alt == False and bool_detectNonFlippers == False:
            return False
        else:
            return True
    
    def __fancyDisplay__():
        global found_flippers
        global data_baseFlippers
        global live_flippers
        FlipDetection.__getLoggedFlippers__()
        allign_center = 10
        print(art_ascii)
        print(f"[FLIPPER NAME]\t\t\t[MAC ADDRESS]\t\t[RSSI]\t\t[FIRST SEEN]\t\t[LAST SEEN]\t\t[TYPE]\t\t[LIVE]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for flipper in data_baseFlippers:
            if len(flipper['Name']) > 15:
                flipper['Name'] = flipper['Name'][:15]
            if flipper['MAC'] in live_flippers:
                if FlipDetection.__detectFlipperBoo__(flipper['isFlipper']) == True:
                    print(flipper['Name'].ljust(allign_center) + "\t\t\t" + flipper['MAC'].ljust(allign_center) + "\t" + str(flipper['RSSI']).ljust(allign_center) + "\t" + flipper['Time First Seen'].ljust(allign_center) + "\t" + flipper['Time Last Seen'].ljust(allign_center) + "\t" + flipper['Detection Type'].ljust(allign_center) + "\tTRUE")
            else:
                if FlipDetection.__detectFlipperBoo__(flipper['isFlipper']) == True:
                    print(flipper['Name'].ljust(allign_center) + "\t\t\t" + flipper['MAC'].ljust(allign_center) + "\t" + str(flipper['RSSI']).ljust(allign_center) + "\t" + flipper['Time First Seen'].ljust(allign_center) + "\t" + flipper['Time Last Seen'].ljust(allign_center) + "\t" + flipper['Detection Type'].ljust(allign_center) + "\tFALSE")
        live_flippers = []
    def __scan__():
        try:
            if FlipDetection.__inLinux__() == True and FlipDetection.__inRoot__() == True:
                scanner = Scanner()
                devices = scanner.scan(0.8)
                for dev in devices:
                    for (adtype, desc, value) in dev.getScanData():
                        if (desc == "Complete Local Name"):
                            if "Flipper" in value:
                                record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                random_flipper_name = value
                                flipper_full_name = random_flipper_name
                                flipper_rssi = dev.rssi
                                flipper_mac = dev.addr
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        found_flippers.remove(flipper) 
                                arrTemp = {
                                    "Name": str(flipper_full_name),
                                    "MAC": str(flipper_mac),
                                    "RSSI": str(flipper_rssi) + " dBm",
                                    "Detection Type": "UID",
                                    "Time Last Seen": str(record_time),
                                    "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                    "isFlipper": True
                                }
                                allowFlipperProxy = True
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        allowFlipperProxy = False

                                if allowFlipperProxy:
                                    live_flippers.append(str(flipper_mac))
                                    found_flippers.append(arrTemp)
                                    FlipDetection.__logFlipper__(flipper_full_name,arrTemp)      
                            elif "80:e1:26" in dev.addr:
                                    record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                    random_flipper_name = value
                                    flipper_full_name = random_flipper_name
                                    flipper_rssi = dev.rssi
                                    flipper_mac = dev.addr
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            found_flippers.remove(flipper)
                                    arrTemp = {
                                        "Name": str(flipper_full_name),
                                        "MAC": str(flipper_mac),
                                        "RSSI": str(flipper_rssi) + " dBm",
                                        "Detection Type": "UIDv2",
                                        "Time Last Seen": str(record_time),
                                        "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                        "isFlipper": True
                                    }
                                    allowFlipperProxy = True
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            allowFlipperProxy = False

                                    if allowFlipperProxy == True:
                                        live_flippers.append(str(flipper_mac))
                                        found_flippers.append(arrTemp)
                                        FlipDetection.__logFlipper__(flipper_full_name,arrTemp)  
                            else:
                                record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                random_flipper_name = value
                                flipper_full_name = random_flipper_name
                                flipper_rssi = dev.rssi
                                flipper_mac = dev.addr
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        found_flippers.remove(flipper)
                                arrTemp = {
                                    "Name": str(flipper_full_name),
                                    "MAC": str(flipper_mac),
                                    "RSSI": str(flipper_rssi) + " dBm",
                                    "Detection Type": "UIDv3",
                                    "Time Last Seen": str(record_time),
                                    "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                    "isFlipper": False
                                }
                                allowFlipperProxy = True
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        allowFlipperProxy = False
                                if allowFlipperProxy == True:
                                    live_flippers.append(str(flipper_mac))
                                    found_flippers.append(arrTemp)
                                    FlipDetection.__logFlipper__(flipper_full_name,arrTemp)  

            else:
                return "Err, something went wrong with validation"
        except (RuntimeError, TypeError, NameError) as e:
                FlipDetection.__warn__("Encountered an error while scanning for devices. Error: " + str(e))
if __name__ == '__main__':
    while True:
        os.system("clear || cls")
        data_baseFlippers = []
        FlipDetection.__fancyDisplay__()
        FlipDetection.__scan__()
        time.sleep(1)



                
