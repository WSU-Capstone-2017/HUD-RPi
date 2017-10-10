README:

Hardware Required:
1. Raspberry Pi
2. Aftermarket head unit (Note: Must support Auxiliary input)
3. Plugable USB Bluetooth 4.0 Low Energy Micro Adapter 
4. 2A Car Supply / Switch or Micro USB Car Charger
5. ELM327 Bluetooth Adapter or ELM327 USB Cable
6. RCA cable 
7. Keyboard

Step 1: Purchase CanaKit - Raspberry Pi3 Complete Starter Kit-32 GB Edition

	Install Raspbian (Comes preinstalled on SD card included within CanaKit)
	
Step 2: Run terminal. Update and upgrade the RPi

	#  sudo apt-get update
	
	#  sudo apt-get upgrade
	
	#  sudo apt-get autoremove
	
	#  sudo reboot
	
Step 3: Run terminal upon restart. Install components.

	#  sudo apt-get install python-serial
	
	#  sudo apt-get install bluetooth bluez-utils blueman
	
	#  sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev
	
	#  sudo apt-get install git-core
	
	#  sudo reboot 
