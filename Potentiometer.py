from machine import ADC, Pin
from utime import sleep

#Constant
BUILT_IN_LED_PIN = const(2)
POT_PIN = const (32)		# ADC1 is GPIO 32 (32-39)
MAX_DELAY = .5 				# seconds

# global variables
delay = 0

# setup
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)
pot = ADC(Pin(POT_PIN, Pin.IN))

# Loop
while True:
    pot_value = pot.read_u16() # read the value from the pot
    delay = pot_value/65025 * MAX_DELAY
    print("delay:", delay)
    if delay > 0:
        print("frequency (toggles per second):", 1/delay)
    led.value(1) # turn on the LED
    sleep(delay) # leave it on for 1/2 second
    led.value(0) # Turn off the LED
    sleep(delay) # leave it off for 1/2 second