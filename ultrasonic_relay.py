#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import numpy as np
import syft as sy

key = "JCLM61DVBH64A6L1"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN_TRIGGER = 18
PIN_ECHO = 27
PIN_INPUT1=25
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.setup(PIN_INPUT1,GPIO.OUT)
GPIO.setup(PIN_INPUT1,GPIO.LOW)

def distance():
     GPIO.output(PIN_TRIGGER, GPIO.HIGH)
     time.sleep(0.00001)
     GPIO.output(PIN_TRIGGER, GPIO.LOW)
     pulse_start_time = time.time()
     pulse_end_time = time.time()
     while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
     while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
     pulse_duration = pulse_end_time - pulse_start_time
     distance = round(pulse_duration * 17150, 2)
     return distance


if __name__ == '__main__':
    ed = dist()
    try:
        while True:
            dist = distance()
            print("Calculating distance",dist)
            if dist<50:
                print("BULBS ON")
                GPIO.output(PIN_INPUT1,GPIO.LOW)
                time.sleep(5)
            else:
                print("BULBS OFF")
                GPIO.output(PIN_INPUT1,GPIO.HIGH)

            #Diff privacy
            rand = np.random.randint(low=1, high =100, size=1)
            if(rand>50):
                dist += np.random.laplace()

            params = urllib.urlencode({'field1':dist,'key':key})
            headers = {"Content-typZZe" : "application/x-www-form-urlencode" , "Accept":"text/plain"}
            conn = httplib.HTTPConnection("api.thingspeak.com:80")

            try:
                conn.request("POST","/update",params, headers)
                response = conn.getresponse()
                print(response.status, response.reason)
                data = response.read()
                conn.close()
            except:
                print("Connection failed")

    except KeyboardInterrupt:
          print("Keyboard Interrupt encountered")

#GPIO.cleanup()
