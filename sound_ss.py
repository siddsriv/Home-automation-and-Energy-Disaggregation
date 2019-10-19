#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
channel = 19
LED = 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(LED,GPIO.LOW)

def callback(channel):
    if GPIO.input(channel):
        print("Sound detected")
        GPIO.output(LED,GPIO.HIGH)
    else:
        print("Sound not detected")
        GPIO.output(LED,GPIO.LOW)
        
GPIO.add_event_detect(channel, GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)

while True:
    time.sleep(1)
    
GPIO.cleanup()    
