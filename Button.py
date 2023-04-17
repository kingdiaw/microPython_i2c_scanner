from machine import Pin
import time

#Constant
BUILT_IN_LED_PIN = const(2)
PB1 = const (15)

#Variable
toggle = 0;

# Setup
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)
button = Pin(PB1, Pin.IN, Pin.PULL_UP) 

# Loop
while True:
    if button.value() == 0: # if the value changes
        toggle ^= 1
        led.value (toggle)
        time.sleep(0.2) # wait 1/50th of a second