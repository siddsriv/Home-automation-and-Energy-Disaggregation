import RPi.GPIO as GPIO
import time
import numpy as np
import syft as sy

key = "R9FB48PHZDKVH0JK"

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
mq2_dpin = 26
mq2_apin = 0
buzz = 4
#port init
def init():
         GPIO.setwarnings(False)
         GPIO.cleanup()         #clean up at the end of your script
         GPIO.setmode(GPIO.BCM)     #to specify whilch pin numbering system
         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         GPIO.setup(mq2_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
         GPIO.setup(buzz,GPIO.OUT)
         GPIO.output(buzz,GPIO.LOW)
#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
#main ioop
def main():
         init()
         print("please wait...")
         time.sleep(5)
         while True:
                  COlevel=readadc(mq2_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)

                  if GPIO.input(mq2_dpin):
                           print("Gas not leak")
                           GPIO.output(buzz, GPIO.LOW)
                           time.sleep(5)
                  else:
                      print("Current Gas AD vaule = " +str("%.2f"%((COlevel/1024.)*3.3))+" V")
                      GPIO.output(buzz,GPIO.HIGH)
                      time.sleep(5)
                  #Diff privacy
                  rand = np.random.randint(low=1, high =100, size=1)
                  if(rand>50):
                      dist += np.random.laplace()

                  params = urllib.urlencode({'field1':COlevel,'key':key})
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

if __name__ =='__main__':
         try:
                  main()

         except KeyboardInterrupt:
                  pass

GPIO.cleanup()
