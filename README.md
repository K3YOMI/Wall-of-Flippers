<p align="center">
 <img src="https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/b524372d-17ef-4e2a-b6fb-ab4fccaaa643" alt="Wall of Flippers"></a>
</p>





<h1 style='font-size: 65px'; align="center">Wall of Flippers</h1>

<div align="center">
  	<p align = "center">🐬 A simple and easy way to find Flipper Zero Devices and Bluetooth Low Energy Based Attacks 🐬</p>
  	<p align = "center">🐬 Documentation written by @k3yomi 🐬</p>
	<div align="center" style="border: none;">
		<table align="center" style="border-collapse: collapse; margin: 0 auto;">
			<tr align="center">
				<td align="center">
					<a href="https://ko-fi.com/k3yomi" style="text-decoration: none;">
						<img align="center" src='https://avatars.githubusercontent.com/u/54733885?s=55&v=4' width="55" height="55">
						<img align="center" src='https://ko-fi.com/img/githubbutton_sm.svg'>
					</a>
					<h3 align="center">k3yomi (Project Maintainer)</h3>
				</td>
				<td align="center">
					<a href="https://ko-fi.com/emilia0001" style="text-decoration: none;">
						<img align="center" src='https://avatars.githubusercontent.com/u/37256246?s=55&v=4' width="55" height="55", style="border-radius: 50%;">
						<img align="center" src='https://ko-fi.com/img/githubbutton_sm.svg'>
					</a>
					<h3 align="center">Emilia (jbohack) (Contributor)</h3>
				</td>
			</tr>
		</table>
		<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/K3YOMI/Wall-of-Flippers">
		<img alt="GitHub forks" src="https://img.shields.io/github/forks/K3YOMI/Wall-of-Flippers">
		<img alt="GitHub issues" src="https://img.shields.io/github/issues/K3YOMI/Wall-of-Flippers">
		<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/K3YOMI/Wall-of-Flippers">
		<a href="https://discord.gg/Bg2fvmjQvg" style="text-decoration: none;">
			<img src="https://discord.com/api/guilds/1190160512953094235/widget.png?style=shield" alt="Discord Shield"/>
		</a>
	</div>
</div>

---

<h1>🐬 Table of Contents</h1>

<div>
    <img align="right" height="490vh" src="https://github.com/K3YOMI/Wall-of-Flippers/assets/54733885/a146acc6-7786-4406-b818-36a48b29473d">
    <img align="right" height="490vh" src="https://upload.wikimedia.org/wikipedia/commons/3/3d/1_120_transparent.png">

</div>




- [Introduction](#doc_introduction)
- [Features](#doc_features)
- [Videos](#doc_videos)
- [Install Guide](#doc_install)
  	- [How to install](#install_guides)
    	- [Debian Linux Install](#debian_install)
    	- [Fedora Install](#fedora_install)
    	- [Arch Linux Install (SOON)](#arch_install)
  		- [Windows Install](#windows_install)
- [Headless Usage](#headless_usage)
- [Issues and Fixes](#doc_issues_and_fixes)
- [Common Errors and Fixes](#doc_c_and_e)
- [Related Projects](#doc_related)
- [Notice](#doc_statement)
- [Credits and Packages](#doc_credits)

<br><br>



# 🐬 Wall of Flippers? <a name = "doc_introduction"></a>
> Wall of Flippers (WoF) is a python based project involving the discovery of the Flipper Zero device and the identification of potential Bluetooth advertisement attacks. Please keep in mind that these two types of detections may **not** be related. Also the code is quite messy and not up to my standards. Will be updating and cleaning up some code in the future. Feel free to submit pull requests if you would like to contribute!



# 🐬 Current features and future updates <a name = "doc_features"></a>
- [x] Discover Flipper Zero Devices (Bluetooth must be enabled)
- [X] Flipper Name Discovery
- [X] Flipper Address Discovery
- [X] Flipper "Identifier" Discovery ( Transparent, White, & Black Flipper Detection)
- [x] Ability to archive past flipper zero devices discovered
- [x] Auto-install functionality for Debian Linux and Windows
- [x] Ability to identify potential Bluetooth Advertisement attacks
	- [x] Suspected Advertisement Attacks
	- [x] ~iOS Crash Advertisement Attack~
	- [x] iOS Popup Advertisement Attacks
	- [x] Samsung and Android BLE Advertisement Attacks
	- [x] Windows Swift Pair Advertisement Attacks
	- [x] LoveSpouse Advertisement Attacks (Denial of Pleasure)
- [ ] ~Capture the Flippers (CTF)~ - (Removed)
- [ ] ~BLE Advertisements~ (Removed)
- [x] BLE External / Internal Adapter Support
	- [x] Linux Supported
 	- [ ] Windows Supported 	
- [ ] Chromium Web Bluetooth Support
- [ ] iOS/Android Detection (Pairing)
- [ ] Animations (Looking for ascii artists)
- [ ] ~Nuclear Fusion Implementation~


# 🐬 Videos and Articles <a name = "doc_videos"></a>

<table align="center" style="border-collapse: collapse; margin: 0 auto;">
	<tr align="center">
		<td align="center">
			<a href="https://www.youtube.com/watch?v=Pnw-uqd0GFM" style="text-decoration: none;">
				<img align="center" src='https://i.ytimg.com/vi/Pnw-uqd0GFM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDEjuLtwBo0n-zRWhAKep7Raon5_Q' width="225" height="155">
			</a>
			<h3 align="center">Talking Sasquach - Wall of Flippers Busts Flipper Zero BLE Spammers Red Handed!</h3>
		</td>
		<td align="center">
			<a href="https://www.bleepingcomputer.com/news/security/wall-of-flippers-detects-flipper-zero-bluetooth-spam-attacks/" style="text-decoration: none;">
				<img align="center" src='https://www.bleepstatic.com/content/hl-images/2023/01/03/flipper-zero.jpg' width="225" height="155", style="border-radius: 50%;">
			</a>
			<h3 align="center">BleepingComputer - ‘Wall of Flippers’ detects Flipper Zero Bluetooth spam attacks</h3>
		</td>
	</tr>
</table>



# 🐬 Installing and Requirements <a name = "doc_install"></a>

> A few things are required to properly run Wall of Flippers. We Recommend a Raspberry Pi as it's compact and portable! It's also required to have a `chipset` or a USB `adapter` that supports Bluetooth Low Energy. At this current time, there is `limited` support for Wall of Flippers on Windows. Hence we recommend using a linux based operating system as that has been used for testing and development. For BLE advertising, I recommened an external USB adapter as the internal adapter on the Raspberry Pi is not powerful enough to send BLE advertisements long range.  



## How to install <a name = "install_guides"></a>

</details>

<details>
<summary> Debian Linux Install Guide </summary>


### Debian Linux Install Guide <a name = "debian_install"></a>
> Wall of Flippers on debian linux is currently one of the best ways to run Wall of Flippers. Mostly due to it being stable and having a lot of support for BTLE. To start off, is is highly recommened to follow all instructions we provide unless you know what you are doing. To get started, we need to set up the directory and install the required packages.

### Step 1 (One): Full system upgrade / update
> Before we continue with the installation, we need to make sure our system is up to date. To do this update through the command line.

	sudo apt-get update && sudo apt-get upgrade -y

### Step 2 (Two): Git Clone and Git Installiation 
> To start off, we need to clone the repository and install the required packages. To do this, we need to run the following commands in the terminal. However, if you do not have git installed, you can simply install it by running this command (apt package manager only): 

	sudo apt-get install git
	git clone https://www.github.com/K3YOMI/Wall-of-Flippers
	cd ./Wall-of-Flippers

### Step 3 (Three): Installing python (python3)
> Installing python3 is required to run wall of flippers and installs it's dependencies. The command below will install python3 for you. 

	sudo apt-get install python3
 	sudo apt-get install python3-dev

### Step 4 (Four): Setting up and Installing the required packages (Multiple Ways)
> Installing the required packets and dependencies can be done in three ways with this install. You can choose to use the terminal with the commands below, use requirements.txt, or you use the easy install script within Wall of Flippers. The choice is up to you depending on your preference. To get started with the terminal way. We will use these commands below.

	sudo apt-get install libglib2.0-dev
 	sudo apt-get install python3-bluez
	python3 -m venv .venv
	source .venv/bin/activate
	################## PACKAGES ########################
	# requirement.txt method
	python3 -m pip install -r requirements.txt
	# command method
	python3 -m pip install bluepy
 	python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
	################## PACKAGES ########################
	deactivate
	
> If you would like to use the easy install script, you can use the following commands below.

	bash wof.sh
	# You should get a prompt upon startup, about setting up a managed environment, feel free to let it do for you. Then once an environemnet is complete run `wof.sh` again
	and press 4 for the auto install process.

### Step 5 (Five): Running Wall of Flippers
> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

	bash wof.sh

> Please keep note that running Wall of Flippers requires elevated privileges. Hence the `sudo` command. If you do not want to run Wall of Flippers with elevated privileges, you can run the following command below.

	sudo chmod +x WallofFlippers.py
	./WallofFlippers.py
 </details>
 <details>
<summary> Fedora Linux Install Guide </summary>
	 
### Fedora Install Guide <a name = "fedora_install"></a>
> To start off, is is highly recommened to follow all instructions we provide unless you know what you are doing. To get started, we need to set up the directory and install the required packages.

### Step 1 (One): Full system upgrade / update
> Before we continue with the installation, we need to make sure our system is up to date. To do this update through the command line.

	sudo dnf update && sudo dnf upgrade -y
### Step 2 (Two): Git Clone and Git Installiation 
> To start off, we need to clone the repository and install the required packages. To do this, we need to run the following commands in the terminal. However, if you do not have git installed, you can simply install it by running this command (apt package manager only): 

	sudo dnf install git
	git clone https://www.github.com/K3YOMI/Wall-of-Flippers
	cd ./Wall-of-Flippers

### Step 3 (Three): Installing python (python3)
> Installing python3 is required to run wall of flippers and installs it's dependencies. The command below will install python3 for you. 

	sudo dnf install python3
 	sudo dnf install python3-dev

### Step 4 (Four): Setting up and Installing the required packages (Multiple Ways)
> Installing the required packets and dependencies can be done in three ways with this install. You can choose to use the terminal with the commands below, use requirements.txt, or you use the easy install script within Wall of Flippers. The choice is up to you depending on your preference. To get started with the terminal way. We will use these commands below.

	sudo dnf install glib2-devel
 	sudo dnf install python3-bluez
	python3 -m venv .venv
	source .venv/bin/activate
	################## PACKAGES ########################
	# requirement.txt method
	python3 -m pip install -r requirements.txt
	# command method
	python3 -m pip install bluepy
 	python3 -m pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
	################## PACKAGES ########################
	deactivate

> If you would like to use the easy install script, you can use the following commands below.

	bash wof.sh
	# You should get a prompt upon startup, about setting up a managed environment, feel free to let it do for you. Then once an environemnet is complete run `wof.sh` again
	and press 4 for the auto install process.

### Step 5 (Five): Running Wall of Flippers
> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

	bash wof.sh

> Please keep note that running Wall of Flippers requires elevated privileges. Hence the `sudo` command. If you do not want to run Wall of Flippers with elevated privileges, you can run the following command below.

	sudo chmod +x WallofFlippers.py
	./WallofFlippers.py


</details>

<details>
<summary> Windows Install Guide </summary>

## Windows Install Guide <a name = "windows_install"></a>
> Windows is currently not fully supported. However, you can still run Wall of Flippers on Windows. A few missing features like the ability to detect advertisement attacks and ability to send advertisements. However the detection of the Flipper Zero device is still supported. To get started, we will need to clone the repository and install the required packages. To do this, we need to run the following commands in the command prompt. However, if you do not have git installed, you can simply install it by downloading it from the official website.

### Step 1 (One): Git Clone and Git Installiation 


	Download Link: https://git-scm.com/downloads

> Once you have downloaded git, you can now run the following commands below.

	git clone https://www.github.com/K3YOMI/Wall-of-Flippers
	cd ./Wall-of-Flippers


### Step 2 (Two): Installing python and pip (python / pip)
> This step is quite straightforward as we will be installing python and pip. To do this, we will need to download the latest version of python from the official website. Once you have downloaded the installer, you can run it and install python. Please make sure to check the box that says `Add Python to PATH`. This will allow you to run python from the command prompt. Once you have installed python, you can now install the required packages. 

	Download Link: https://www.python.org/downloads/

> Once you have installed python, you can now install the required packages. To do this, we will need to run the following commands below.

	pip install bleak


> Alternatively, you can use the requirements.txt file to install the required packages. To do this, we will need to run the following commands below.

	pip install -r requirements.txt

> If you would like to use the easy install script, you can use the following commands below.

	python WallofFlippers.py
	# You should get a prompt upon startup, press 4 for the easy install and follow the directions and prompts for the install.

> If you are having issues with pip being not recognized as a command, please refer to this question below:\
https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command

### Step 3 (Three): Running Wall of Flippers
> Once you have finished with all the dependencies and requirements, you can now run Wall of Flippers. To do this, you can run the following command below.

	python WallofFlippers.py
	
> Please keep note that this is a watered down version of Wall of Flippers. Hence the lack of features. If you would like to run the full version of Wall of Flippers, please refer to the Linux Install Guide above.


</details>

# Headless Usage <a name = "headless_usage"></a>
> Wall of Flippers now supports the use of a command only interface. Thanks to @cyberartemio for the recommendation. The commands below can be used to automate the use the Wall of Flippers. Whether that be for systemd or just basic general automation. (If you are running/using a virtual environment, make sure to source to be able to use WallofFlippers.py)

	usage: WalloFlippers.py [-h] [-w] [i] [-d DEVICE]
	options:
	-h, --help					Help Message
	-w, --wall 					Wall of Flippers
	-i, --install				Install Dependencies
	-d DEVICE, --device DEVICE	A bluetooth device (External/Internal)

# Issues and Fixes <a name = "doc_issues_and_fixes"></a>
> If you encounter any issues or bugs, please report them to us on our github page. We will try our best to fix them as soon as possible. If you would like to contribute to the project, please feel free to make a pull request. We will review it and merge it if it is a good addition to the project. We will be starting a discord server soon for support and development. Please keep an eye out for that. Thank you for your support and we hope you enjoy this project! <3


# Common Errors and Fixes <a name = "doc_c_and_e"></a>
### No such file or directory /sys/class/bluetooth
> If the `/sys/class/bluetooth` directory is not present on your system, it may indicate that the Bluetooth subsystem is not properly detected or enabled. To check if you have the right hardware, please run 

	sudo service bluetooth status

> If the status is `dead` you may not have a valid bluetooth chipset or adapter present. If `inactive`, you can enable the service using this command

	sudo service bluetooth restart

### pybluez failing to properly install
> If you're experiencing issues while installing `pybluez`, make sure to install the python-dev package. For further documentation (https://pybluez.readthedocs.io/en/latest/install.html)


# Related Projects <a name = "doc_related"></a>
> A list of repositories that have integrated Wall of Flippers (WoF) into their projects.

**Pwnagotchi plugin**\
*Written by: cyberartemio*\
https://github.com/cyberartemio/wof-pwnagotchi-plugin

**Evil-M5Core2**\
*Written by: 7h30th3r0n3*\
https://github.com/7h30th3r0n3/Evil-M5Core2


# Notice <a name = "doc_statement"></a>
> This project isn't the solution to combat the Flipper Zero device or any form of btle attacks. **THIS DOES NOT MITIGATE OR STOP ANYTHING**!!! However, the flipper zero device is a great tool for learning and understanding the inctracies of the cyberworld. Now for the detections for this project, we heavily rely on the advertisements that the Flipper Zero sends out for detection. While a user can do many things to avoid being detected by Wall of Flippers. (Depending if the Identifier method gets worked around) We highly advise using this project for an end all solution. While not all bluetooth attacks are sent from only the flipper, it's a good start to understand the world of bluetooth and the attacks that can be accomplished with simple devices. We hope you enjoy this project and we hope you take the time to learn and build off of this. We are always looking for contributions and new ideas. Thank you for looking at this project and we hope you enjoy it! -k3yomi and emilia0001








# Contributors and Credits <a name = "doc_credits"></a>
> This project was made possible by the following people. Please make sure to check them out and support them! <3

| Project Maintainer | Project Contributor | AppleJuice BLE Advertisement Data |
| --- | --- | --- |
| ![k3yomi](https://avatars.githubusercontent.com/u/54733885?s=55&v=4) | ![emilia0001](https://avatars.githubusercontent.com/u/37256246?s=55&v=4) | ![ecto-1a](https://avatars.githubusercontent.com/u/112792126?s=55&v=4)
| k3yomi | emilia0001 | Ecto-1A |
