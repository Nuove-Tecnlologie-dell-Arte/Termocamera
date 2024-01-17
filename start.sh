#!/bin/bash
cd /home/pi/LeptonModule/software/raspberrypi_video
sudo sh -c "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"
./raspberrypi_video -tl 3 &
cd /usr/bin/
obs 
