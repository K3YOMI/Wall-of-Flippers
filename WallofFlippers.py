
# bluepy library (https://github.com/IanHarvey/bluepy/blob/master/README.md)

#   What is Wall of Flippers? 
#   Wall of Flippers (WoF) is a Python based project designed for Bluetooth Low Energy (BTLE) exploration. 
#   Its primary functionality involves the discovery of the Flipper Zero and the identification of potential BTLE based attacks

# Thanks for all the support, feels very welcoming to see people interested in this project! - Kiyomi + Emilia

dolphin_thinking = [
    'Let\'s hunt some flippers', 
    "Ya'll like war driving flippers?", 
    "Skid detector 9000",
    "I'm a flipper, you're a flipper, we're all flippers!",
    "Flipper Zero : Advanced Warefare",
    "Don't be a skid!!!!!!",
    "discord.gg/squachtopia",
    "Hack the planet!",
]
with open('ascii.txt', 'r', encoding="utf8") as f:
    ascii = f.read()




wof_data = { # I just hold important data
    "found_flippers": [], # (IGNORE)
    "data_baseFlippers": [], # (IGNORE)
    "live_flippers": [], # (IGNORE)
    "display_live": [], # (IGNORE)
    "display_offline": [], # (IGNORE)
    "max_online": 30, # Max online devices to display
    "max_offline": 30, # Max offline devices to display
    "bool_scanning": False, # (IGNORE)
    "forbidden_packets_found": [], # (IGNORE)
    "system_type": None, # (IGNORE)
    "forbidden_packets": [ # Not complete and feel free to add more ("_" = Random Value)
        {"PCK": "4c000f05c_________000010______", "TYPE": "BLE_APPLE_IOS_CRASH_LONG"},
        {"PCK": "4c000719010_2055__________________________________________", "TYPE": "BLE_APPLE_DEVICE_POPUP_CLOSE"},
        {"PCK": "4c000f05c00_______", "TYPE": "BLE_APPLE_ACTION_MODAL_LONG"},
        {"PCK": "2cfe______", "TYPE": "BLE_ANDROID_DEVICE_CONNECT"},
        {"PCK": "750042098102141503210109____01__063c948e00000000c700", "TYPE": "BLE_SAMSUNG_BUDS_POPUP_LONG"},
        {"PCK": "7500010002000101ff000043__", "TYPE": "BLE_SAMSUNG_WATCH_PAIR_LONG"},
        {"PCK": "0600030080________________________", "TYPE": "BLE_WINDOWS_SWIFT_PAIR_SHORT"},
        {"PCK": "ff006db643ce97fe427_______", "TYPE": "BLE_LOVE_TOYS_SHORT_DISTANCE"},
    ]                                                  
}





class FlipperUtils: # meow meow, I dislike this class
    def __asciiArt__():
        print(ascii.replace("[RANDOM_QUOTE]", random.choice(dolphin_thinking)))
    def __convertHowLongAgo__(timey):
        currentTime = int(time.time())
        timeAgo = currentTime - timey
        minutes = str(timeAgo // 60) + "m"
        seconds = str(timeAgo % 60) + "s"
        return f"{(minutes)} {(seconds)}"
    def __logFlipper__(name, data): 
        with open('Flipper.json', 'r') as db:
            file_data = json.load(db)
        for flipper in file_data:
             if flipper['MAC'] == data['MAC']:
                flipper['RSSI'] = data['RSSI']
                flipper['Detection Type'] = data['Detection Type']
                flipper['unixLastSeen'] = data['unixLastSeen']
                flipper['Spoofing'] = data['Spoofing']
                with open('Flipper.json', 'w') as f:
                    json.dump(file_data, f, indent=4)
                return
        file_data.append(data)
        with open('Flipper.json', 'w') as f:
               json.dump(file_data, f, indent=4)
    def __fancyDisplay__():
        global wof_data
        with open('Flipper.json', 'r') as db:
            file_data = json.load(db)
        wof_data['data_baseFlippers'].extend(flipper for flipper in file_data)
        allign_center = 8
        for flipper in wof_data['data_baseFlippers']:
            flipper['Name'] = flipper['Name'].replace("Flipper ", "")[:15]
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
        if wof_data['system_type'] == "posix":
            if wof_data['forbidden_packets_found']:
                print("Notice: These attacks may not be related to the Flipper Zero.\n")
                print(f"[NAME]\t\t\t\t\t[ADDR]\t\t   [PACKET]")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                for packet in wof_data['forbidden_packets_found']:
                    total_ble = total_ble + 1
                    if total_ble <= 10:
                        name = packet['Type']
                        mac = packet['MAC']
                        pkt = packet['PCK']
                        print(name.ljust(allign_center) +   "\t\t" +  mac.ljust(allign_center) + "  " + pkt.ljust(allign_center))
            if len(wof_data['forbidden_packets_found']) > 25:
                print(f"━━━━━━━━━━━━━━━━━━ Bluetooth Low Energy (BLE) Attacks Detected ({len(wof_data['forbidden_packets_found'])}+ Packets) ━━━━━━━━━━━━━━━━━━━━")
        else:
            print(f"━━━━━━━━━━━━━━━━━━ BLE Attack Detection is still in development for Windows. ━━━━━━━━━━━━━━━━━━━━")
        print(f"\n\n[FLIPPER]".ljust(8)+ "\t" +"[ADDR]".ljust(8)+ "\t\t" +"[FIRST]".ljust(8)+ "\t" +"[LAST]".ljust(8)+ "\t" +"[RSSI]".ljust(8)+ "\t" +"[SPOOFING]".ljust(8))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if wof_data['display_live']:
            print("(ONLINE DEVICES)".center(100))
            for flipper in wof_data['display_live']:
                totalLive += 1
                if totalLive < wof_data['max_online']:
                    print(flipper['Name'].ljust(8)+ "\t" + flipper['MAC']+ "\t" + str(FlipperUtils.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(8) + "\t" + str(FlipperUtils.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(8) + "\t" + str((flipper['RSSI'])) +"".ljust(8) + "\t" + str(flipper['Spoofing']).ljust(8) )
                if totalLive == wof_data['max_online'] - 1:
                    totalLiveStr = len(wof_data['display_live']) - wof_data['max_online']
                    print(f"Too many <online> devices to display. ({totalLiveStr} devices)".center(100))
                    break
        if wof_data['display_offline']:
            wof_data['display_offline'] = sorted(wof_data['display_offline'], key=lambda k: k['unixLastSeen'], reverse=True)
            print("(OFFLINE DEVICES)".center(100))
            for flipper in wof_data['display_offline']:
                totalOffline += 1
                if totalOffline < wof_data['max_offline']:
                    print( flipper['Name'].ljust(8)+ "\t" + flipper['MAC']+ "\t" + str(FlipperUtils.__convertHowLongAgo__(flipper['unixFirstSeen'])).ljust(8) + "\t" + str(FlipperUtils.__convertHowLongAgo__(flipper['unixLastSeen'])).ljust(8)+ "\t" + "-".ljust(8)+ "\t" + str(flipper['Spoofing']).ljust(8))
                if totalOffline == wof_data['max_offline'] - 1:
                    totalOfflineStr = len(wof_data['display_offline'])  - wof_data['max_offline']
                    print(f" Too many <offline> devices to display. ({totalOfflineStr} devices)".center(100))
                    break
        wof_data['display_live'] = []
        wof_data['display_offline'] = []
        wof_data['live_flippers'] = []
        wof_data['forbidden_packets_found'] = []

class FlipDetection:
    async def run_detection_async(os_type): # F*ck it, lets make it async and make it one function
        wof_data['bool_scanning'] = True
        ble_packets = []
        if os_type == "nt":
            devices = await BleakScanner.discover() # Windows Supported BLE Package (Non-Cross-Platform packages scare me)
            for device in devices:
                adv_name = device.name
                adv_addr = device.address.lower()
                adv_rssi =  device.rssi
                adv_packet = device.metadata.get("manufacturer_data", "DATA_I_DONT_CARE_TO_LOOK_AT_BECAUSE_ITS_VERY_LONG")
                ble_packets.append({"Name": adv_name, "MAC": adv_addr, "RSSI": adv_rssi, "PCK": adv_packet})
        if os_type == "posix":
            scanner = Scanner() # Linux Supported BLE Package 
            devices = scanner.scan(5)
            for device in devices:
                for (adv_type, adv_description, adv_value) in device.getScanData():
                    adv_name = adv_value
                    if adv_description == "Complete Local Name":
                        adv_addr = device.addr.lower()
                        adv_rssi = device.rssi
                        ble_packets.append({"Name": adv_name, "MAC": adv_addr, "RSSI": adv_rssi, "PCK": adv_value})
                    elif not any(device.addr.lower().startswith(addr) for addr in ("80:e1:26", "80:e1:27")):
                        adv_addr = device.addr.lower()
                        adv_rssi = device.rssi
                        ble_packets.append({"Name": adv_name, "MAC": adv_addr, "RSSI": adv_rssi, "PCK": adv_value})
        for packet in ble_packets: # I'm sorry for this code... I'm not proud of it either
            adv_name = packet['Name']
            adv_addr = packet['MAC']
            adv_rssi = packet['RSSI']
            adv_packet = packet['PCK']
            ble_blacklist_check = ""
            the_wall_of_forbidden_packets = wof_data['forbidden_packets']
            for packet in the_wall_of_forbidden_packets:
                bool_isSimilar = True
                packet_value = packet['PCK']
                packet_type = packet['TYPE']
                ble_blacklist_check = packet_value
                total_underscores = ble_blacklist_check.count("_")
                total_found = 0
                for char1, char2 in zip(adv_packet, ble_blacklist_check):
                    if char2 != '_' and char1 != char2:
                        bool_isSimilar = False
                    if char1 == char2:
                        total_found += 1
                if bool_isSimilar:
                    get_non_underscore_chars = len(ble_blacklist_check) - total_underscores
                    if total_found == get_non_underscore_chars:
                        wof_data['forbidden_packets_found'].append({"MAC": adv_addr, "PCK": adv_packet, "Type": packet_type})

            if adv_name == "Flipper":
                adv_recorded = int(time.time())
                for adv_device in wof_data['found_flippers']:
                    if adv_device['MAC'] == adv_addr: wof_data['found_flippers'].remove(adv_device)
                data = {"Name": adv_name,"MAC": adv_addr,"RSSI": adv_rssi,"Detection Type": "Flipper","Spoofing": True,"unixFirstSeen": adv_recorded,"unixLastSeen": adv_recorded}
                is_added = all(adv_device['MAC'] != adv_addr for adv_device in wof_data['found_flippers'])
                if is_added:
                    wof_data['live_flippers'].append(adv_addr)
                    wof_data['found_flippers'].append(data)
                    FlipperUtils.__logFlipper__(adv_name,data)
            elif any(adv_addr.startswith(addr) for addr in ("80:e1:26", "80:e1:27")): # If there are any other valid Flipper MAC addresses, please let me know asap. : D
                adv_recorded = int(time.time())
                for adv_device in wof_data['found_flippers']:
                    if adv_device['MAC'] == adv_addr: wof_data['found_flippers'].remove(adv_device)
                data = {"Name": adv_name,"MAC": adv_addr,"RSSI": adv_rssi,"Detection Type": "Flipper","Spoofing": True,"unixFirstSeen": adv_recorded,"unixLastSeen": adv_recorded}
                is_added = all(adv_device['MAC'] != adv_addr for adv_device in wof_data['found_flippers'])
                if is_added:
                    wof_data['live_flippers'].append(adv_addr)
                    wof_data['found_flippers'].append(data)
                    FlipperUtils.__logFlipper__(adv_name,data)
            wof_data['bool_scanning'] = False


import os,time,json,random,asyncio # Importing all the required modules (Windows and Linux modules are different)
os.system("clear || cls")
system_type = os.name
wof_data['system_type'] = system_type
if system_type == "nt": from bleak import BleakScanner # Windows BLE Package
if system_type == "posix": from bluepy.btle import Scanner # Linux BLE Package
if system_type == "posix" and os.geteuid() != 0: print("[!] Wall of Flippers >> WoF requires root privileges to run.\n\t      Reason: Dependency on bluepy library."); exit() # Check if the user is root (Linux)
while True:
    if not wof_data['bool_scanning']:
        wof_data['data_baseFlippers'] = []
        FlipperUtils.__fancyDisplay__()
        asyncio.run(FlipDetection.run_detection_async(system_type))
    time.sleep(0.1) # Don't worry about this - Everything is fine... :P

