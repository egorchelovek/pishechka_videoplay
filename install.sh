#!/bin/bash

echo "Install Pishechka Videoplay..."

# Prepare software
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
sudo pip3 install omxplayer-wrapper

# Copy data
sudo mkdir /opt/pishechka_videoplay
sudo cp -R data /opt/pishechka_videoplay
sudo cp program.py /opt/pishechka_videoplay

# Init on startup
sudo cp pishechka.sh /etc/init.d
sudo chmod +x /etc/init.d/pishechka.sh
sudo update-rc.d pishechka.sh defaults

# Don't forget GPU mem
sudo echo gpu_mem=128 >> /boot/config.txt

echo "All done. It should work after reboot. Enjoy it!"
