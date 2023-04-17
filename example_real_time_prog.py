# Real-time embedded programming
# https://pypi.org/project/pcf8574-library/
# https://docs.micropython.org/en/latest/library/time.html
#import related library
import time
from machine import Pin
from PCF8574 import PCF8574, P0, P1, P2

#Declare Constant Value
SDA_PIN = const (21)
SCL_PIN = const (22)
PCF1_ADDRESS = const (0x20)

#Mapping Object
pcf = PCF8574(PCF1_ADDRESS, sda=SDA_PIN, scl=SCL_PIN)

#Variable
task1_interval = time.ticks_add (time.ticks_ms(), 500)
task2_interval = time.ticks_add (time.ticks_ms(), 1000)
task3_interval = time.ticks_add (time.ticks_ms(), 2000)
led1_state = False
led2_state = False
led3_state = False

#Setup
pcf.Pin(P0, Pin.OUT)
pcf.Pin(P1, Pin.OUT)
pcf.Pin(P2, Pin.OUT)
#loop
while True:
    if time.ticks_diff (task1_interval, time.ticks_ms())<= 0:
        led1_state ^= 1
        task1_interval = time.ticks_add(time.ticks_ms(),500)
        pcf.digital_write(P0, led1_state)

    if time.ticks_diff (task2_interval, time.ticks_ms())<= 0:
        led2_state ^= 1
        task2_interval = time.ticks_add(time.ticks_ms(),1000)
        pcf.digital_write(P1, led2_state)

    if time.ticks_diff (task3_interval, time.ticks_ms())<= 0:
        led3_state ^= 1
        task3_interval = time.ticks_add(time.ticks_ms(),2000)
        pcf.digital_write(P2, led3_state)
