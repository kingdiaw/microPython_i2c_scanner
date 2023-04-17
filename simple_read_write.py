# https://pypi.org/project/pcf8574-library/
#import related library
import time
from machine import Pin
from PCF8574 import PCF8574, P0, P1

#Mapping Object
pcf = PCF8574(0x20, sda=21, scl=22)

#Setup
pcf.Pin(P0, Pin.IN)
pcf.Pin(P1, Pin.OUT)

#loop
while True:
    buttonState = pcf.digital_read(P0)
    print ("PB1 State= " + str(buttonState))
    if buttonState == 0:
        pcf.digital_write(P1,1)
    else:
        pcf.digital_write(P1,0)
    time.sleep(1)
