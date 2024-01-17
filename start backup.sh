#!/bin/bash
sudo python fratm.py &
cd ..
cd LeptonModule/software/raspberrypi_video
sudo sh -c "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
./raspberrypi_video -tl 3 &
cd /usr/bin/
obs &
cd ..
cd ..
cd /home/pi/Desktop/ 
sudo python mouse.py &
