#!/bin/bash
if pgrep -x "xcompmgr" > /dev/null
then
    echo "Already Running"
else
    echo "Stopped; starting xcompmgr now"
    DISPLAY=:0 xcompmgr &
fi
sleep 5
#check for network availability?
while ! ping -c 1 -W 1 8.8.8.8; do
    echo "Waiting for 8.8.8.8 - network interface might be down..."
    sleep 1
done

# DISPLAY=:0 xcompmgr &
sleep 2
# DISPLAY=:0 python3 main.py
# (DISPLAY=:0 /usr/bin/python3 /home/pi/Media-Scheduler/Firmware/main.py >/home/pi/Media-Scheduler/Firmware/main_logs.txt 2>&1)
cd /home/pi/Media-Scheduler/Firmware
DISPLAY=:0 python3 main.py > /home/pi/Media-Scheduler/Firmware/main_logs.txt 2>&1