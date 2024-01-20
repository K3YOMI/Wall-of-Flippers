<p align="center">
	<img src="https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/b524372d-17ef-4e2a-b6fb-ab4fccaaa643" alt="Wall of Flippers" />
</p>

<h1 align="center">Wall of Flippers</h1>

<div align="center">
  	<p align = "center">🐬 A simple and easy way to find Flipper Zero Devices and Bluetooth Low Energy Based Attacks 🐬</p>
  	<p align = "center">🐬 Documentation written by @k3yomi 🐬</p>
	<div align="center">
		<table align="center">
			<tr align="center">
				<td align="center">
					<a href="https://ko-fi.com/k3yomi">
						<img align="center" src="https://avatars.githubusercontent.com/u/54733885?s=55&v=4" alt="avatar" width="55" height="55" />
						<img align="center" src="https://ko-fi.com/img/githubbutton_sm.svg" alt="kofi" />
					</a>
					<h3 align="center">k3yomi (Project Maintainer)</h3>
				</td>
				<td align="center">
					<a href="https://ko-fi.com/emilia0001">
						<img align="center" src="https://avatars.githubusercontent.com/u/37256246?s=55&v=4" alt="avatar" width="55" height="55" />
						<img align="center" src="https://ko-fi.com/img/githubbutton_sm.svg" alt="kofi" />
					</a>
					<h3 align="center">Emilia (jbohack) (Contributor)</h3>
				</td>
			</tr>
		</table>
		<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/K3YOMI/Wall-of-Flippers" />
		<img alt="GitHub forks" src="https://img.shields.io/github/forks/K3YOMI/Wall-of-Flippers" />
		<img alt="GitHub issues" src="https://img.shields.io/github/issues/K3YOMI/Wall-of-Flippers" />
		<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/K3YOMI/Wall-of-Flippers" />
		<a href="https://discord.gg/Bg2fvmjQvg">
			<img src="https://discord.com/api/guilds/1190160512953094235/widget.png?style=shield" alt="Discord Shield" />
		</a>
	</div>
</div>

---

<div>
    <img align="right" height="490vh" src="https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/a146acc6-7786-4406-b818-36a48b29473d" alt="wof" />
</div>

# Table of Contents
- [Introduction](#-introduction)
- [Features](#-current-features-and-future-updates)
- [Videos and Articles](#-videos-and-articles)
- [Install Guide](#-installing-and-requirements)
  	- [How to install](#how-to-install)
- [Issues and Fixes](#issues-and-fixes)
- [Common Errors and Fixes](#common-errors-and-fixes)
- [Notice](#notice)
- [Contributors](#contributors)
- [Credits](#credits)

<br />
<br />
<br />
<br />

# 🐬 Introduction

> Wall of Flippers (WoF) is a python based project involving the discovery of the Flipper Zero device and the identification of potential Bluetooth advertisment attacks. Please keep in mind that these two types of detections may **not** be related. Also the code is quite messy and not up to my standards. Will be updating and cleaning up some code in the future. Feel free to submit pull requests if you would like to contribute!

# 🐬 Current features and future updates

- [x] Discover Flipper Zero Devices (Bluetooth must be enabled)
- [X] Flipper Name Discovery
- [X] Flipper Address Discovery
- [X] Flipper "Identifier" Discovery ( Transparent, White, & Black Flipper Detection)
- [x] Ability to archive past flipper zero devices discovered
- [x] Auto-install functionality for Debian Linux and Windows
- [x] Ability to identify potential Bluetooth advertisment attacks
	- [x] Suspected Advertisment Attacks
	- [x] ~iOS Crash Advertisment Attack~ (Patched as of the latest iOS update)
	- [x] iOS Popup advertisment Attacks
	- [x] Samsung and Andorid BLE Advertisment Attacks
	- [x] Windows Swift Pair Advertisment Attacks
	- [x] LoveSpouse Advertisment Attacks (Denial of Pleasure)
- [ ] Capture the Flippers (CTF) - A simple CTF to collect Flipper Zero devices
	- [x] Leaderboard
	- [ ] Hosting Support (Local and Public)
	- [ ] Ability to add custom challenges
	- [x] Point System and Scoring
	- [x] Username and Key System
- [x] BLE Advertisments
	- [x] Ability to send custom BLE advertisments
- [x] BLE External / Internal Adapter Support
	- [x] Linux Supported
 	- [ ] Windows Supported 	
- [ ] Chromium Web Bluetooth Support
- [ ] iOS/Android Detection (Pairing)
- [ ] Animations (Looking for ascii artists)
- [ ] ~Nuclear Fusion Implementation~


# 🐬 Videos and Articles

<table align="center">
	<tr align="center">
		<td align="center" width="49%">
			<a href="https://www.youtube.com/watch?v=Pnw-uqd0GFM">
				<img align="center" src="https://i.ytimg.com/vi/Pnw-uqd0GFM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDEjuLtwBo0n-zRWhAKep7Raon5_Q" width="225px" />
			</a>
		</td>
		<td align="center" width="49%">
			<a href="https://www.bleepingcomputer.com/news/security/wall-of-flippers-detects-flipper-zero-bluetooth-spam-attacks/">
				<img align="center" src="https://www.bleepstatic.com/content/hl-images/2023/01/03/flipper-zero.jpg" width="225px" />
			</a>
		</td>
	</tr>
	<tr>
		<td align="center" width="49%">
			<p align="center">Talking Sasquach - Wall of Flippers Busts Flipper Zero BLE Spammers Red Handed!</p>
		</td>
		<td align="center" width="49%">
			<p align="center">BleepingComputer - ‘Wall of Flippers’ detects Flipper Zero Bluetooth spam attacks</p>
		</td>
	</tr>
</table>

# 🐬 Installing and Requirements

> A few things are required to properly run Wall of Flippers. We Recommend a Raspberry Pi as it's compact and portable! It's also required to have a `chipset` or a USB `adapter` that supports Bluetooth Low Energy. At this current time, there is `limited` support for Wall of Flippers on Windows. Hence we recommend using a linux based operating system as that has been used for testing and development. For BLE advertising, I recommened an external USB adapter as the internal adapter on the Raspberry Pi is not powerful enough to send BLE advertisments long range.  

## How to install

<details>
<summary>Debian Linux Install Guide</summary>

### Debian Linux Install Guide

> Wall of Flippers on debian linux is currently one of the best ways to run Wall of Flippers. Mostly due to it being stable and having a lot of support for BLE. To start off, it is highly recommened to follow all instructions we provide unless you know what you are doing. To get started, we need to set up the directory and install the required packages.

#### Step 1: Full system upgrade / update

> Before we continue with the installation, we need to make sure our system is up to date. To do this update through the command line.

```sh
sudo apt-get update && sudo apt-get upgrade -y
```

#### Step 2: Git Clone and Git Installiation

> To start off, we need to clone the repository and install the required packages. To do this, we need to run the following commands in the terminal. However, if you do not have git installed, you can simply install it by running this command (apt package manager only): 

```sh
sudo apt-get install git
git clone https://www.github.com/K3YOMI/Wall-of-Flippers
cd ./Wall-of-Flippers
```

#### Step 3: Installing python (python3)

> Installing python3 is required to run wall of flippers and installs it's dependencies. The command below will install python3 for you. 

```sh
sudo apt-get install python3
```

#### Step 4: Setting up and Installing the required packages (Multiple Ways)

> Installing the required packets and dependencies can be done in three ways with this install. You can choose to use the terminal with the commands below, use requirements.txt, or you use the easy install script within Wall of Flippers. The choice is up to you depending on your preference. To get started with the terminal way. We will use these commands below.

```sh
sudo apt-get install libglib2.0-dev
sudo apt-get install python3-bluez
python3 -m venv .venv
source .venv/bin/activate

################## PACKAGES ########################
# requirement.txt method
python3 -m pip install -r requirements.txt
# command method
python3 -m pip install bluepy
python3 -m pip install requests
python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
################## PACKAGES ########################

deactivate
```

> If you would like to use the easy install script, you can use the following commands below.

```sh
bash wof.sh
```

> You should get a prompt upon startup, about setting up a managed environment, feel free to let it do for you. Then once an environemnet is complete run `wof.sh` again and press 4 for the auto install process.

#### Step 5: Running Wall of Flippers

> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

```sh
bash wof.sh
```

> Please keep note that running Wall of Flippers requires elevated privileges. Hence the `sudo` command. If you do not want to run Wall of Flippers with elevated privileges, you can run the following command below.

```sh
sudo chmod +x WallofFlippers.py
./WallofFlippers.py
```

</details>
 
<details>
<summary>Fedora Linux Install Guide</summary>
	 
### Fedora Install Guide

> To start off, is is highly recommened to follow all instructions we provide unless you know what you are doing. To get started, we need to set up the directory and install the required packages.

#### Step 1: Full system upgrade / update

> Before we continue with the installation, we need to make sure our system is up to date. To do this update through the command line.

```sh
sudo dnf update && sudo dnf upgrade -y
```

#### Step 2: Git Clone and Git Installiation 

> To start off, we need to clone the repository and install the required packages. To do this, we need to run the following commands in the terminal. However, if you do not have git installed, you can simply install it by running this command (apt package manager only): 

```sh
sudo dnf install git
git clone https://www.github.com/K3YOMI/Wall-of-Flippers
cd ./Wall-of-Flippers
```

#### Step 3: Installing python (python3)

> Installing python3 is required to run wall of flippers and installs it's dependencies. The command below will install python3 for you. 

```sh
sudo dnf install python3
```

#### Step 4: Setting up and Installing the required packages (Multiple Ways)

> Installing the required packets and dependencies can be done in three ways with this install. You can choose to use the terminal with the commands below, use requirements.txt, or you use the easy install script within Wall of Flippers. The choice is up to you depending on your preference. To get started with the terminal way. We will use these commands below.

```sh
sudo dnf install glib2-devel
sudo dnf install python3-bluez
python3 -m venv .venv
source .venv/bin/activate

################## PACKAGES ########################
# requirement.txt method
python3 -m pip install -r requirements.txt
# command method
python3 -m pip install bluepy
python3 -m pip install requests
python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
################## PACKAGES ########################

deactivate
```

> If you would like to use the easy install script, you can use the following commands below.

```sh
bash wof.sh
```

> You should get a prompt upon startup, about setting up a managed environment, feel free to let it do for you. Then once an environemnet is complete run `wof.sh` again and press 4 for the auto install process.

#### Step 5: Running Wall of Flippers

> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

```sh
bash wof.sh
```

> Please keep note that running Wall of Flippers requires elevated privileges. Hence the `sudo` command. If you do not want to run Wall of Flippers with elevated privileges, you can run the following command below.

```sh
sudo chmod +x WallofFlippers.py
./WallofFlippers.py
```

</details>

<details>
<summary>Windows Install Guide</summary>

### Windows Install Guide

> Windows is currently not fully supported. However, you can still run Wall of Flippers on Windows. A few missing features like the ability to detect advertisment attacks and ability to send advertisments. However the detection of the Flipper Zero device is still supported. To get started, we will need to clone the repository and install the required packages. To do this, we need to run the following commands in the command prompt. However, if you do not have git installed, you can simply install it by downloading it from the official website.

#### Step 1: Git Clone and Git Installiation 

> Download and install `git` from [here](https://git-scm.com/downloads). Once you have downloaded it, you can now run the following commands below.

```powershell
git clone https://www.github.com/K3YOMI/Wall-of-Flippers
cd ./Wall-of-Flippers
```

#### Step 2: Installing python and pip (python / pip)

> This step is quite straightforward as we will be installing python and pip. To do this, we will need to download the latest version of python from the [official website](https://www.python.org/downloads/). Once you have downloaded the installer, you can run it and install python. Please make sure to check the box that says `Add Python to PATH`. This will allow you to run python from the command prompt. Once you have installed python, you can now install the required packages. To do this, we will need to run the following commands below.

```powershell
pip install bleak
pip install requests
```

> Alternatively, you can use the requirements.txt file to install the required packages. To do this, we will need to run the following commands below.

```powershell
pip install -r requirements.txt
```

> If you would like to use the easy install script, you can use the following commands below.

```powershell
python WallofFlippers.py
```
> You should get a prompt upon startup, press 4 for the easy install and follow the directions and prompts for the install.
>
> If you are having issues with pip being not recognized as a command, please refer to [this](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command) question on Stack Overflow.

#### Step 3: Running Wall of Flippers

> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

```powershell
python WallofFlippers.py
```
	
> Please keep note that this is a watered down version of Wall of Flippers. Hence the lack of features. If you would like to run the full version of Wall of Flippers, please refer to the Linux Install Guide above.

</details>

# Issues and Fixes

> If you encounter any issues or bugs, please report them to us on our github page. We will try our best to fix them as soon as possible. If you would like to contribute to the project, please feel free to make a pull request. We will review it and merge it if it is a good addition to the project. We will be starting a discord server soon for support and development. Please keep an eye out for that. Thank you for your support and we hope you enjoy this project! <3


# Common Errors and Fixes

### No such file or directory `/sys/class/bluetooth`

> If the `/sys/class/bluetooth` directory is not present on your system, it may indicate that the Bluetooth subsystem is not properly detected or enabled. To check if you have the right hardware, please run:

```sh
sudo service bluetooth status
```

> If the status is `dead` you may not have a valid bluetooth chipset or adapter present. If `inactive`, you can enable the service using this command

```sh
sudo service bluetooth restart
```

# Notice

> This project isn't the solution to combat the Flipper Zero device or any form of BLE attacks. **THIS DOES NOT MITIGATE OR STOP ANYTHING**!!! However, the flipper zero device is a great tool for learning and understanding the inctracies of the cyberworld. Now for the detections for this project, we heavily rely on the advertisments that the Flipper Zero sends out for detection. While a user can do many things to avoid being detected by Wall of Flippers. (Depending if the Identifier method gets worked around) We highly advise using this project for an end all solution. While not all bluetooth attacks are sent from only the flipper, it's a good start to understand the world of bluetooth and the attacks that can be accomplished with simple devices.
> 
> We hope you enjoy this project and we hope you take the time to learn and build off of this. We are always looking for contributions and new ideas. Thank you for looking at this project and we hope you enjoy it!
> 
> *k3yomi and emilia0001*

# Contributors

> This project was made possible by the following people. Please make sure to check them out and support them! <3

[<img alt="K3YOMI" src="https://avatars.githubusercontent.com/u/54733885?v=4&s=55" width="55">](https://github.com/K3YOMI) |[<img alt="nescapp" src="https://avatars.githubusercontent.com/u/97590612?v=4&s=55" width="55">](https://github.com/nescapp) |[<img alt="jbohack" src="https://avatars.githubusercontent.com/u/37256246?v=4&s=55" width="55">](https://github.com/jbohack) |[<img alt="OnlyNandan" src="https://avatars.githubusercontent.com/u/78302872?v=4&s=55" width="55">](https://github.com/OnlyNandan) |[<img alt="cyberartemio" src="https://avatars.githubusercontent.com/u/156206062?v=4&s=55" width="55">](https://github.com/cyberartemio) |[<img alt="AleksaMCode" src="https://avatars.githubusercontent.com/u/23129943?v=4&s=55" width="55">](https://github.com/AleksaMCode) |[<img alt="elliotwutingfeng" src="https://avatars.githubusercontent.com/u/30223404?v=4&s=55" width="55">](https://github.com/elliotwutingfeng) |
:---: |:---: |:---: |:---: |:---: |:---: |:---: |
[K3YOMI](https://github.com/K3YOMI) |[nescapp](https://github.com/nescapp) |[jbohack](https://github.com/jbohack) |[OnlyNandan](https://github.com/OnlyNandan) |[cyberartemio](https://github.com/cyberartemio) |[AleksaMCode](https://github.com/AleksaMCode) |[elliotwutingfeng](https://github.com/elliotwutingfeng) |

# Credits

AppleJuice BLE Advertisment Data |
:---: |
[<img alt="ecto-1a" src="https://avatars.githubusercontent.com/u/112792126" width="55">](https://github.com/ECTO-1A) |
[ECTO-1A](https://github.com/ECTO-1A)|

# Stargazers over time

[![Stargazers over time](https://starchart.cc/K3YOMI/Wall-of-Flippers.svg?variant=light)](https://starchart.cc/K3YOMI/Wall-of-Flippers)