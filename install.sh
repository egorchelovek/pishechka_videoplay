#!/bin/bash

sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
sudo pip3 install omxplayer-wrapper
sudo echo "sudo python /home/pi/pishechka_videoplay/program.py start" >> /home/pi/.bashrc
