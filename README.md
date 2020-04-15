"Appify" your E46 BMW with a Raspberry Pi and your Smartphone! This repository contains the IBUS controller, as well as the Android application which supports smart phones and wearables. This is to be used with the IBUS USB interface which can be acquired from [Reslers.de](http://www.reslers.de/IBUS/), or from Amazon/eBay.

## Overview 

There are three main components of the solution:
* Android Tablet - Primary front-end device for interacting with the car
* Raspberry Pi - Mini-PC that handles communication between the IBUS adapter and the Android device
* IBUS USB Adapter - USB adapter that provides USB/UART interface from physical wire in car

![Android_RPi_IBUS_Overview](https://s3-us-west-1.amazonaws.com/connected-car-static-files/connected_car_overview2.png)

There is also an Android Wear (4.4W) component that allows you to control your vehicle from your smart watch!
* Android Wear Device - Secondary device that provides quick interactions with the car

![Android_WEAR_IBUS_Overview](https://s3-us-west-1.amazonaws.com/connected-car-static-files/IBUS+Wear+UI+On+G+Watch.png)

## Pre-Requisites
### 1. Car Installation
* Remove OEM Navigation Head Unit from BMW
* Tap the 12V (red) wire, the GND (black) wire, and the IBUS (red/white/yellow) wire
* Connect IBUS USB adapter to BMW (using 12V, GND, IBUS)
* Install USB 12V - 5V adapter (using 12V, GND)
* Install Raspberry Pi in the dash (and power w/ 5V from adapter)
* Connect IBUS USB adapter to Raspberry Pi via USB cable
* Connect Ethernet cable to Raspberry Pi (and wire to glove box)

### 2. Raspberry Pi

* Install packages
	* `sudo apt-get install build-essential bluetooth bluez bluez-tools libbluetooth-dev`
* Download project
	* `git clone https://github.com/TC60225/RASPI-IBUS-Controller.git`
	* `cd RASPI-IBUS-Controller/connected_car_controller`
* Install python modules:
	* `pip install -r requirements.txt`
* Run the project: `python3 start_controller.py R53`

### 3. Android Mobile / Tablet
* Update `BluetoothInterface.remoteBluetoothAddress` of 'connected_car_app/common' with RPi Bluetooth address
* Build Android project `connected_car_app/` via Android Studio
* Install the applicaton
	* You can build and run in Android Studio by connecting your devices
	* You can also install by transfering the built APKs 
		* `connected_car_app/app/build/outputs/apk/debug/app-debug.apk`
		* `connected_car_app/ibuswear/build/outputs/apk/debug/ibuswear-debug.apk`

## How To Get Started
* Install the prerequisites above
* Ensure Android device is paired with Raspberry Pi via Bluetooth
* Run the controller as daemon: `docker-compose up -d`
* Launch Connected Car App on your Android device or wearable
