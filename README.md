# Wall of Flippers (WoF)
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
                a8888'                      `Y8888P' `V888888    
              d8888888a                                `Y8888           
             AY/'' `\Y8b                                 ``Y8b
             Y'      `YP                                    ~~
     _       __      ____         ____   _________                           
    | |     / /___ _/ / /  ____  / __/  / ____/ (_)___  ____  ___  __________
    | | /| / / __ `/ / /  / __ \/ /_   / /_  / / / __ \/ __ \/ _ \/ ___/ ___/
    | |/ |/ / /_/ / / /  / /_/ / __/  / __/ / / / /_/ / /_/ /  __/ /  (__  ) 
    |__/|__/\__,_/_/_/   \____/_/    /_/   /_/_/ .___/ .___/\___/_/  /____/ 
                                              /_/   /_/

## 💡 Introduction
Wall of Flippers (WoF) is a Python based project designed for Bluetooth Low Energy (BTLE) exploration. Its primary functionality involves the discovery of the Flipper Zero device and the identification of potential BTLE based attacks.
Please keep in mind this is a work in progress and will still continue to get updates.


## 🛠️ Features
- Flipper Zero Detection (BT Must be Enabled)
- Flipper Archiving (Saving Past Data)
- Bluetooth Low Energy Attacks
  - iOS Crash and Popup BTLE Detection
  - Android Crash and Popup BTLE Detection
  - Windows Swift Pair BTLE Detection
  - LoveSpouse BTLE Detection
_______
![ezgif-4-eadf27922b](https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/9e0aeef5-962e-4e0c-b4d5-0b6163441c5c)
_______

## 💡 Future Improvements
- GoLang Support
- hcidump / hcitool support



## 📚 Some Documentation


### Requirements
A few things are required to properly run WoF. We Recommend the Raspberry Pi as its compact and portable! Additionally, it's also required to have a `chipset` or a USB `adapter` that supports BTLE.
Additionally, we also now have *limited* support for Windows and *full* support for linux at this time. 

## Linux Install Guide

Another `requirement` is Python. Debian based install:


    $ sudo apt-get install python3

Additionally, bluepy `requires` the `libglib2.0-dev` library to be installed. Debian based install:

    $ sudo apt-get install python3-pip libglib2.0-dev

Finally, `bluepy` is required. This can be installed with the following command:

    $ sudo pip3 install bluepy

*Your install may look different depending if python3 is used*\
*Additionally, if you are having trouble. Feel free to visit this repo for better documentation: https://github.com/IanHarvey/bluepy/*



### Git Clone and Running
  Alright, it's fun for the fun install process. Downloading WoF is quite straightforward as it's a few commands. 
  I'd recommend using `git` as this command can be easily used to retrieve the repository. Otherwise, just donwload via GitHub.

    $ git clone https://github.com/K3YOMI/Wall-of-Flippers

  After installing, navigate to the Wall of Flippers directory

    $ cd ./Wall\ of\ Flippers

  Next, run under `sudo` as this part is required to properly use the `pyblue` functionality.

    $ sudo python3 WallofFlippers.py 



## Windows Install Guide
  Another `requirement` is Python. Windows Based Below:\
  https://www.python.org/

  `bleak` is required. This can be installed with the following command:

    $ pip install bleak

  Additional commands may need to be ran for pip to run properly. see: https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command

  *Your install may look different depending if py is used*\
  *Additionally, if you are having trouble. Feel free to visit this repo for better documentation: https://github.com/hbldh/bleak*

  ### Git Clone and Running
  Alright, it's fun for the fun install process. Downloading WoF is quite straightforward as it's a few commands. 
  I'd recommend using `git` as this command can be easily used to retrieve the repository. Otherwise, just donwload via GitHub.
  
    $ git clone https://github.com/K3YOMI/Wall-of-Flippers
    
  After installing, navigate to the Wall of Flippers directory
  
    $ cd ./Wall\ of\ Flippers

  Next, run this command below to start the python script and wallah! You are now running Wall of Flippers!

    $ py WallofFlippers.py 


  ### Conclusion

  Tad-ah! You are now properly running WoF on your device. Hopefully this small guide works and gets you started on collecting flippers or checking for
  BTLE based attacks. Feel free to report bugs as this can help improve WoF. You can modify, release, or use Wall of Flippers in any way you want
  as long as proper credit is given to `emilia (jbohack)` and `k3yomi (kiyomi)`. Thank you!


  ## Notice (Please Read)
  This project isn't the solution for catching every Bluetooth Low Energy (BLE) attack or Flipper Zero device. Users can easily dodge detection by changing their device's MAC address or name, or simply turning off Bluetooth. The main purpose here is keeping track of activity to catch a few "script kiddies" now and then. It's not foolproof, but it's a useful tool for identifying issues and figuring out how often devices are being misused. The real goal is to encourage updates for vulnerable devices, so they can't be exploited in the future. While this project doesn't stop attacks, logging is a crucial step in understanding device issues and abuse patterns. If you have any questions or concerns about bluetooth or the project itself, don't hesitate to reach out to me!

  
![Untitled2](https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/a146acc6-7786-4406-b818-36a48b29473d)

### Support Kiyomi (Developer)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/k3yomi)
### Support Emilia (Contributor)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/emilia0001)



