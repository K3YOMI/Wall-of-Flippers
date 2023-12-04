
# bluepy library (https://github.com/IanHarvey/bluepy/blob/master/README.md)

#   What is Wall of Flippers? 
#   Wall of Flippers (WoF) is a Python based project designed for Bluetooth Low Energy (BTLE) exploration. 
#   Its primary functionality involves the discovery of the Flipper Zero and the identification of potential BTLE based attacks


#  How to use?
#       1. Install libglib2.0-dev (sudo apt-get install python-pip libglib2.0-dev) 
#       2. Install bluepy (sudo pip install bluepy)
#       3. Run the script (sudo python WallofFlippers.py)




import os,time,json,random
from bluepy.btle import Scanner

dolphin_thinking = [
    'Let\'s hunt some flippers', 
    "uWu, I see a flipper nearby!", 
    "I have been deployed owo", 
    "Ya'll like war driving flippers?", 
    "I was made with love and care",
    "Please stop annoying people with your flipper...",
    "Script kiddie detector 9000",
    "This video is sponsored by PCBWay!!!",
    "I'm a flipper, you're a flipper, we're all flippers!",
    "Please refrain from annoying people with your flipper...",
    "My VIBRO Motor go brrrrrzz5rzrrz",
    "Fun fact: Astro is a synesthesiac moon deer 🤯",
    "Flipper Zero : Advanced Warefare",
    "Why does my flipper make a ticking noise with the RGB Mod??!?!",
    "No, you can not control traffic lights. Stop asking....",
    "Don't be a skid!!!!!!",
    "yo put a lily quote in there - lily",
    "discord.gg/squachtopia",
]
ascii = open('ascii.txt', 'r').read()




wof_data = { # I just hold important data
    "found_flippers": [], # (IGNORE)
    "data_baseFlippers": [], # (IGNORE)
    "live_flippers": [], # (IGNORE)
    "display_live": [], # (IGNORE)
    "display_offline": [], # (IGNORE)
    "max_online": 30, # Max online devices to display
    "max_offline": 15, # Max offline devices to display
    "bool_scanning": False, # (IGNORE)
    "forbidden_packets_found": [], # (IGNORE)
    "forbidden_packets": [ # You can add your own packet detection here (optional)
        {"PCK": "4c000f05", "TYPE": "BLE_APPLE_IOS_CRASH_LONG"},
        {"PCK": "4c00071901122055", "TYPE": "BLE_APPLE_DEVICE_POPUP_CLOSE"},
        {"PCK": "4c000f05c0", "TYPE": "BLE_APPLE_ACTION_MODAL_LONG"},
        {"PCK": "0000fe2c-0000-1000-8000-00805f9b34fb", "TYPE": "BLE_ANDROID_DEVICE_CONNECT"},
        {"PCK": "75004209810214150321010985010116063c948e00000000c700", "TYPE": "BLE_SAMSUNG_BUDS_POPUP_LONG"},
        {"PCK": "7500010002000101ff000043", "TYPE": "BLE_SAMSUNG_WATCH_PAIR_LONG"},
        {"PCK": "0600030080", "TYPE": "BLE_WINDOWS_SWIFT_PAIR_SHORT"},
        {"PCK": "ff006db643ce97fe427c", "TYPE": "BLE_LOVE_TOYS_VIBRATE_SHORT"},
        {"PCK": "ff006db643ce97fe427ce5157d", "TYPE": "BLE_LOVE_TOYS_DENIAL_SHORT"},
    ]
}





class FlipperUtils:
    def __asciiArt__():
        print(ascii.replace("[RANDOM_QUOTE]", random.choice(dolphin_thinking)))
    def __convertHowLongAgo__(timey):
        currentTime = int(time.time())
        timeAgo = currentTime - timey
        minutes = str(timeAgo // 60) + "m"
        seconds = str(timeAgo % 60) + "s"
        if timeAgo // 60 > 10000:
            minutes = "---"
            seconds = "---"
        return f"{(minutes)} {(seconds)}"
    def __logFlipper__(name, data): 
        db = open('Flipper.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
             if flipper['MAC'] == data['MAC']:
                flipper['Time Last Seen'] = data['Time Last Seen']
                flipper['RSSI'] = data['RSSI']
                flipper['Detection Type'] = data['Detection Type']
                flipper['unixLastSeen'] = data['unixLastSeen']
                flipper['Spoofing'] = data['Spoofing']
                with open('Flipper.json', 'w') as f:
                    json.dump(file_data, f, indent=4)
                db.close()
                return
        file_data.append(data)
        with open('Flipper.json', 'w') as f:
               json.dump(file_data, f, indent=4)
        db.close()
    def __fancyDisplay__():
        global wof_data
        db = open('Flipper.json', 'r')
        file_data = json.load(db)
        for flipper in file_data:
            wof_data['data_baseFlippers'].append(flipper)
        db.close()
        allign_center = 10
        for flipper in wof_data['data_baseFlippers']:
            if len(flipper['Name']) > 15:
                flipper['Name'] = flipper['Name'][:15]
            if flipper['MAC'] in wof_data['live_flippers']:
                wof_data['display_live'].append(flipper)
            else:
                wof_data['display_offline'].append(flipper)
        totalLive = 0
        totalOffline = 0
        os.system("clear || cls")
        FlipperUtils.__asciiArt__()
        print(f"Total Online...: {len(wof_data['display_live'])}")
        print(f"Total Offline..: {len(wof_data['display_offline'])}\n\n")
        total_ble = 0
        if (len(wof_data['forbidden_packets_found']) > 0):
            print(f"[NAME]\t\t\t\t\t[MAC]\t\t   [PACKET]")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            for packet in wof_data['forbidden_packets_found']:
                total_ble = total_ble + 1
                if (total_ble <= 10):
                    name = packet['Type']
                    mac = packet['MAC']
                    pkt = packet['PCK']
                    print(  
                        name.ljust(allign_center) + 
                          "\t\t" +  
                        mac.ljust(allign_center) + "  " + 
                        pkt.ljust(allign_center)
                    )
        if (len(wof_data['forbidden_packets_found']) > 25):
            print(f"━━━━━━━━━━━━━━━━━━ Bluetooth Low Energy (BLE) Attacks Detected ({len(wof_data['forbidden_packets_found'])}+ Packets) ━━━━━━━━━━━━━━━━━━━━")
        print(f"\n\n[NAME]\t\t[MAC]\t\t   [F. TIME]  [L. TIME]  [dBm]    [TYPE]     [SPOOF]   [LIVE]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if (len(wof_data['display_live']) > 0):
            print("( ONLINE DEVICES )".center(95))
            for flipper in wof_data['display_live']:
                totalLive += 1
                if totalLive < wof_data['max_online']:
                    print(  flipper['Name'].ljust(allign_center) + "\t" +  flipper['MAC'].ljust(allign_center) + "  " + str(FlipperUtils.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(allign_center) + " " + str(FlipperUtils.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(allign_center) + " " + str(flipper['RSSI']).ljust(allign_center) + "" + flipper['Detection Type'].ljust(allign_center) + "" + str(flipper['Spoofing']).ljust(allign_center) + "" + "True" )
                if totalLive == wof_data['max_online'] - 1:
                    totalLiveStr = len(wof_data['display_live']) - wof_data['max_online']
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <online> devices to display. ({totalLiveStr} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        if (len(wof_data['display_offline']) > 0):
            # reorganize to show the unix last seen first
            wof_data['display_offline'] = sorted(wof_data['display_offline'], key=lambda k: k['unixLastSeen'], reverse=True)
            print("( OFFLINE DEVICES )".center(95))
            for flipper in wof_data['display_offline']:
                totalOffline += 1
                if totalOffline < wof_data['max_offline']:
                    print( flipper['Name'].ljust(allign_center)+ "\t" + flipper['MAC'].ljust(allign_center)+ "  " + str(FlipperUtils.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(allign_center) + " " + str(FlipperUtils.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(allign_center) + " " + str(flipper['RSSI']).ljust(allign_center) + "" + flipper['Detection Type'].ljust(allign_center) + "" + str(flipper['Spoofing']).ljust(allign_center) + "" + "False")
                if totalOffline == wof_data['max_offline'] - 1:
                    totalOfflineStr = len(wof_data['display_offline'])  - wof_data['max_offline']
                    print(f"━━━━━━━━━━━━━━━━━━ Too many <offline> devices to display. ({totalOfflineStr} devices) ━━━━━━━━━━━━━━━━━━━━")
                    break
        wof_data['display_live'] = []
        wof_data['display_offline'] = []
        wof_data['live_flippers'] = []
        wof_data['forbidden_packets_found'] = []

class FlipDetection:
    def __scan__():
        try:
            scanner = Scanner()
            wof_data['bool_scanning'] = True
            devices = scanner.scan(5)
            for dev in devices:
                for (adtype, desc, value) in dev.getScanData():
                    packet = str(value)
                    for packet in wof_data['forbidden_packets']:
                        name = packet['TYPE']
                        pck = packet['PCK']
                        if (pck in value):
                            wof_data['forbidden_packets_found'].append({"MAC": dev.addr, "Type": name, "PCK": value})
                    if (desc == "Complete Local Name"):
                        if ("Flipper") in value:
                            record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            random_flipper_name = value
                            flipper_full_name = random_flipper_name
                            flipper_rssi = dev.rssi
                            flipper_mac = dev.addr
                            for flipper in wof_data['found_flippers']: 
                                if flipper['MAC'] == flipper_mac: wof_data['found_flippers'].remove(flipper)
                            arrTemp = {"Name": str(flipper_full_name),"MAC": str(flipper_mac),"RSSI": str(flipper_rssi) + " dBm","Detection Type": "Flipper","Spoofing": False,"Time Last Seen": str(record_time),"Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),"unixFirstSeen": int(time.time()),"unixLastSeen": int(time.time()),"isFlipper": True}
                            allowFlipperProxy = True
                            for flipper in wof_data['found_flippers']:
                                if flipper['MAC'] == flipper_mac: allowFlipperProxy = False
                            if allowFlipperProxy:
                                wof_data['live_flippers'].append(str(flipper_mac))
                                wof_data['found_flippers'].append(arrTemp)
                                FlipperUtils.__logFlipper__(flipper_full_name,arrTemp)     
                        elif ("80:e1:26" or "80:e1:27") in dev.addr:
                                record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                random_flipper_name = value
                                flipper_full_name = random_flipper_name
                                flipper_rssi = dev.rssi
                                flipper_mac = dev.addr
                                for flipper in wof_data['found_flippers']: 
                                    if flipper['MAC'] == flipper_mac: wof_data['found_flippers'].remove(flipper)
                                arrTemp = {"Name": str(flipper_full_name),"MAC": str(flipper_mac),"RSSI": str(flipper_rssi) + " dBm","Detection Type": "Flipper","Spoofing": True,"Time Last Seen": str(record_time),"Time First Seen": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),"unixFirstSeen": int(time.time()),"unixLastSeen": int(time.time()),"isFlipper": True}
                                allowFlipperProxy = True
                                for flipper in wof_data['found_flippers']:
                                    if flipper['MAC'] == flipper_mac: allowFlipperProxy = False
                                if allowFlipperProxy == True:
                                    wof_data['live_flippers'].append(str(flipper_mac))
                                    wof_data['found_flippers'].append(arrTemp)
                                    FlipperUtils.__logFlipper__(flipper_full_name,arrTemp)  
            wof_data['bool_scanning'] = False
        except (RuntimeError, TypeError, NameError) as e:
                print("[!] NoFlip >> Encountered an error while scanning for devices. Error: " + str(e))
                wof_data['bool_scanning'] == False
if __name__ == '__main__':
    os.system("clear || cls")
    get_os = os.name
    get_root = os.getuid()
    if (get_os != "posix"):
        print("[!] NoFlip >> WoF is not supported on Windows.\n\t      Reason: Dependency on bluepy library.")
        exit()
    if (get_root != 0):
        print("[!] NoFlip >> WoF requires root privileges to run.\n\t      Reason: Dependency on bluepy library.")
        exit()
    while True:
        if (wof_data['bool_scanning'] == False):
            wof_data['data_baseFlippers'] = []
            FlipperUtils.__fancyDisplay__()
            FlipDetection.__scan__()
        time.sleep(0.1)



                
