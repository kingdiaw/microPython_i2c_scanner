# Setup - run once
from machine import Pin # Get the Pin function from the machine module.
from time import sleep # Get the sleep library from the time module.

# This is the built-in green LED on the ESP32 DEVKIT V1.
BUILT_IN_LED_PIN = const(2)

# The line below indicates we are configuring this as an output (not input)
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

# Main loop: Repeat the forever...
while True:
    led.value(1) # turn on the LED
    sleep(0.5) # leave it on for 1/2 second
    led.value(0)  # Turn off the LED
    sleep(0.5) # leave it off for 1/2 second