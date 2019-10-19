#!/bin/bash

lxterminal -e "/home/pi/Desktop/ultrasonic+relay.py; sleep 10" &
lxterminal -e "/home/pi/Desktop/sound_ss.py; sleep 10" &
lxterminal -e "/home/pi/Desktop/smoke_final.py; sleep 10"