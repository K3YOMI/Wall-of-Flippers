
# All rights reserved to the contributors of the bluepy library. I am not the owner of this library. However, I am the owner of the code below handling
# the bluetooth scanning detection for the Flipper zero device. For any questions / mistakes, please feel free to contact me on my github account @K3YOMI
# Have a blessed day!


#   What is NoFlip? 
#       NoFlip is a simple python script that detects the Flipper Zero device that is used as a multi-tool for ethical hackers.


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
       a8888'                      `Y8888P' `V888888            (K3YOMI && jbohack)
     d8888888a                                `Y8888             * Made With Love *
    AY/'' `\Y8b                                 ``Y8b
    Y'      `YP                                    ~~
     _       __      ____         ____   _________                           
    | |     / /___ _/ / /  ____  / __/  / ____/ (_)___  ____  ___  __________
    | | /| / / __ `/ / /  / __ \/ /_   / /_  / / / __ \/ __ \/ _ \/ ___/ ___/
    | |/ |/ / /_/ / / /  / /_/ / __/  / __/ / / / /_/ / /_/ /  __/ /  (__  ) 
    |__/|__/\__,_/_/_/   \____/_/    /_/   /_/_/ .___/ .___/\___/_/  /____/  
                                              /_/   /_/                                                         
"""



import os,time,random
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle
import json

vendor_list = []
found_flippers = []
data_baseFlippers = []
live_flippers = []
bool_detectNonFlippers = True
bool_exemptRandom = True


display_live = []
display_offline = []


class FlipDetection:
    def __logDevice__(name, data): 
        db = open('Devices.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
             if flipper['MAC'] == data['MAC']:
                flipper['Time Last Seen'] = data['Time Last Seen']
                flipper['RSSI'] = data['RSSI']
                flipper['Detection Type'] = data['Detection Type']
                flipper['unixLastSeen'] = data['unixLastSeen']
                with open('Devices.json', 'w') as f:
                    json.dump(file_data, f, indent=4)
                db.close()
                return
        file_data.append(data)
        with open('Devices.json', 'w') as f:
               json.dump(file_data, f, indent=4)
        db.close()
    def __logFlipper__(name, data): 
        db = open('Flipper.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
             if flipper['MAC'] == data['MAC']:
                flipper['Time Last Seen'] = data['Time Last Seen']
                flipper['RSSI'] = data['RSSI']
                flipper['Detection Type'] = data['Detection Type']
                flipper['unixLastSeen'] = data['unixLastSeen']
                with open('Flipper.json', 'w') as f:
                    json.dump(file_data, f, indent=4)
                db.close()
                return
        file_data.append(data)
        with open('Flipper.json', 'w') as f:
               json.dump(file_data, f, indent=4)
        db.close()
    def __getLoggedFlippers__():
        db = open('Devices.json', 'r')
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
    def __getVendor__(mac):
        mac = mac[:8]
        for vendor in vendor_list:
            if vendor['macPrefix'] == mac:
                return vendor['vendorName']
        return 'Unknown Vendor'
                
        
    def __convertHowLongAgo__(timey):
        currentTime = int(time.time())
        timeAgo = currentTime - timey
        minutes = timeAgo / 60
        seconds = timeAgo % 60
        return f"{int(minutes)}m {int(seconds)}s"
    def __fancyDisplay__():
        global found_flippers
        global data_baseFlippers
        global live_flippers
        global display_live
        global display_offline
        FlipDetection.__getLoggedFlippers__()
        allign_center = 10
        for flipper in data_baseFlippers:
            if len(flipper['Name']) > 15:
                flipper['Name'] = flipper['Name'][:15]
            if flipper['MAC'] in live_flippers:
                if FlipDetection.__detectFlipperBoo__(flipper['isFlipper']) == True:
                    display_live.append(flipper)
            else:
                if FlipDetection.__detectFlipperBoo__(flipper['isFlipper']) == True:
                    display_offline.append(flipper)
        totalLive = 0
        totalOffline = 0
        print(art_ascii)
        print(f"Total Online...: {len(display_live)}")
        print(f"Total Offline..: {len(display_offline)}\n\n")
        print(f"[NAME]\t\t[MAC]\t\t   [F. TIME]  [L. TIME]  [dBm]    [TYPE]     [SPOOF]   [LIVE]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if (len(display_live) > 0):
            print("( ONLINE DEVICES )".center(95))
            for flipper in display_live:
                totalLive += 1
                if totalLive < 30:
                    print( 
                        flipper['Name'].ljust(allign_center)
                        + "\t" + 
                        flipper['MAC'].ljust(allign_center)
                        + "  " +
                        str(FlipDetection.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(allign_center)
                        + " " +
                        str(FlipDetection.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(allign_center)
                        + " " +
                        str(flipper['RSSI']).ljust(allign_center)
                        + "" +
                        flipper['Detection Type'].ljust(allign_center)
                        + "" +
                        str(flipper['Spoofing']).ljust(allign_center)
                        + "" +
                        "TRUE"
                    )
                if totalLive == 29:
                    totalLiveStr = len(display_live) - 30
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <online> devices to display. ({totalLiveStr} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        if (len(display_offline) > 0):
            print("( OFFLINE DEVICES )".center(95))
            for flipper in display_offline:
                totalOffline += 1
                if totalOffline < 20:
                    print( 
                        flipper['Name'].ljust(allign_center)
                        + "\t" + 
                        flipper['MAC'].ljust(allign_center)
                        + "  " +
                        str(FlipDetection.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(allign_center)
                        + " " +
                        str(FlipDetection.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(allign_center)
                        + " " +
                        str(flipper['RSSI']).ljust(allign_center)
                        + "" +
                        flipper['Detection Type'].ljust(allign_center)
                        + "" +
                        str(flipper['Spoofing']).ljust(allign_center)
                        + "" +
                        "FALSE"
                    )
                if totalOffline == 19:
                    totalOfflineStr = len(display_offline)  - 20
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <offline> devices to display. ({totalOfflineStr} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        display_live = []
        display_offline = []
        live_flippers = []
    def __scan__():
        try:
            if FlipDetection.__inLinux__() == True and FlipDetection.__inRoot__() == True:
                scanner = Scanner()
                devices = scanner.scan(5)
                for dev in devices:
                    for (adtype, desc, value) in dev.getScanData():
                        jsonDump = json.dumps(dev.getScanData())
                        if not "Complete Local Name" in jsonDump:
                            if bool_exemptRandom == False:
                                record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                random_flipper_name = value
                                flipper_full_name = FlipDetection.__getVendor__(dev.addr)
                                flipper_rssi = dev.rssi
                                flipper_mac = dev.addr
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        found_flippers.remove(flipper)
                                arrTemp = {
                                    "Name": str(flipper_full_name),
                                    "MAC": str(flipper_mac),
                                    "RSSI": str(flipper_rssi) + " dBm",
                                    "Detection Type": "Vendor",
                                    "Spoofing": False,
                                    "Time Last Seen": str(record_time),
                                    "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                    "unixFirstSeen": int(time.time()),
                                    "unixLastSeen": int(time.time()),
                                    "isFlipper": False
                                }
                                allowFlipperProxy = True
                                for flipper in found_flippers:
                                    if flipper['MAC'] == flipper_mac:
                                        allowFlipperProxy = False
                                if allowFlipperProxy == True:
                                    live_flippers.append(str(flipper_mac))
                                    found_flippers.append(arrTemp)
                                    FlipDetection.__logDevice__(flipper_full_name,arrTemp) 
                            else:
                                if bool_exemptRandom == True and dev.addrType == 'public':
                                    record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                    random_flipper_name = value
                                    flipper_full_name = FlipDetection.__getVendor__(dev.addr)
                                    flipper_rssi = dev.rssi
                                    flipper_mac = dev.addr
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            found_flippers.remove(flipper)
                                    arrTemp = {
                                        "Name": str(flipper_full_name),
                                        "MAC": str(flipper_mac),
                                        "RSSI": str(flipper_rssi) + " dBm",
                                        "Detection Type": "Vendor",
                                        "Spoofing": False,
                                        "Time Last Seen": str(record_time),
                                        "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                        "unixFirstSeen": int(time.time()),
                                        "unixLastSeen": int(time.time()),
                                        "isFlipper": False
                                    }
                                    allowFlipperProxy = True
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            allowFlipperProxy = False
                                    if allowFlipperProxy == True:
                                        live_flippers.append(str(flipper_mac))
                                        found_flippers.append(arrTemp)
                                        FlipDetection.__logDevice__(flipper_full_name,arrTemp) 
                        else:
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
                                        "Detection Type": "Flipper",
                                        "Spoofing": False,
                                        "Time Last Seen": str(record_time),
                                        "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                        "unixFirstSeen": int(time.time()),
                                        "unixLastSeen": int(time.time()),
                                        "isFlipper": True
                                    }
                                    allowFlipperProxy = True
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            allowFlipperProxy = False

                                    if allowFlipperProxy:
                                        live_flippers.append(str(flipper_mac))
                                        found_flippers.append(arrTemp)
                                        FlipDetection.__logDevice__(flipper_full_name,arrTemp) 
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
                                            "Detection Type": "Flipper",
                                            "Spoofing": True,
                                            "Time Last Seen": str(record_time),
                                            "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                            "unixFirstSeen": int(time.time()),
                                            "unixLastSeen": int(time.time()),
                                            "isFlipper": True
                                        }
                                        allowFlipperProxy = True
                                        for flipper in found_flippers:
                                            if flipper['MAC'] == flipper_mac:
                                                allowFlipperProxy = False

                                        if allowFlipperProxy == True:
                                            live_flippers.append(str(flipper_mac))
                                            found_flippers.append(arrTemp)
                                            FlipDetection.__logDevice__(flipper_full_name,arrTemp)  
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
                                        "Detection Type": "Device",
                                        "Spoofing": False,
                                        "Time Last Seen": str(record_time),
                                        "Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                                        "unixFirstSeen": int(time.time()),
                                        "unixLastSeen": int(time.time()),
                                        "isFlipper": False
                                    }
                                    allowFlipperProxy = True
                                    for flipper in found_flippers:
                                        if flipper['MAC'] == flipper_mac:
                                            allowFlipperProxy = False
                                    if allowFlipperProxy == True:
                                        live_flippers.append(str(flipper_mac))
                                        found_flippers.append(arrTemp)
                                        FlipDetection.__logDevice__(flipper_full_name,arrTemp)  

            else:
                return "Err, something went wrong with validation"
        except (RuntimeError, TypeError, NameError) as e:
                FlipDetection.__warn__("Encountered an error while scanning for devices. Error: " + str(e))
if __name__ == '__main__':
    loadFile = open("mac-vendors-export.json", "r")
    loadJson = json.load(loadFile)
    for vendor in loadJson:
        vendor_list.append(vendor)
    loadFile.close()
    while True:
        os.system("clear || cls")
        data_baseFlippers = []
        FlipDetection.__fancyDisplay__()
        FlipDetection.__scan__()
        time.sleep(1)



                
