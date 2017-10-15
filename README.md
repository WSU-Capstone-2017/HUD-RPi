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

Step 4: Run terminal upon restart. Update and Upgrade the RPi in preparation to install Navit.
	# sudo apt-get update
	# sudo apt-get upgrade

Step 5: In terminal, install Navit and all its components
	# sudo apt-get install navit
	# sudo apt-get install navit espeak

Step 6: Copy the default Navit folder under the home directory
	# mkdir ~/.navit
	# cp /etc/navit/navit.xml .navit/navit.xml

Step 7: Download Maps
	# Go to "http://maps9.navit-project.org/" and download your maps
	# Rename the download file from the conventional "osm_bbox....bin" to something more simple 
		Try to rename the file to "<area>.bin"

Step 8: From the root directory make a folder called "maps"
	# mkdir ~/maps
	# mv <area>.bin maps/

Step 9: Navit Config file needs to be edited to include the new map
	#nano ~/.navit/navit.xml
Disable the Sample Map
<!-- If you dont want to use the sample map, either set enabled="no" in the next line or remove the xml file from the maps directory>
<mapset enabled="yes"> (CHANGE THIS TO "no")
	<xi:include href="$NAVIT_SHAREDIR/maps/*.xml"/>
</mapset>

Enable the Downloaded Map
<!-- Mapset template for openstreetmaps -->
<mapset enabled="no"> (CHANGE THIS TO "yes")
	


<map type="binfile" enabled="yes" data="/media/mmc2/MapsNavit/osm_europe.bin"/> 
	(CHANGE THE "data" FIELD TO YOUR RENAMED MAP! (/home/pi/maps/<area>.bin))
</mapset>

Step 10: Change various navit configurations
Enable Speech
<speech type="cmdline" data="echo 'Fix the speech tag in navit.xml to let navit say:' '%s'" cps="15"/>
	(CHANGE THE "data" field to "espeak  '%s' cps="15"")

Change Locale
<config xmlns:xi="https://www.w3.org/2001/XInclude"> 
	(ADD "language="en_US" AT THE END)

Follow Vehicle
<vehicle name="Local GPS" profile name="car" enabled="yes" active="1" source="gpsd://localhost" gpsd_query="w+xj">
	(ADD "follow="2"" at the end)

Disable Points of Interest
<layer name="POI Symbols"> 
	(ADD "enabled="no"" BEFORE THE ">")
	# 
	#
	
	#
	#
	
	