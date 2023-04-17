from machine import ADC, Pin
from utime import sleep

#Constant
POT_PIN = const (32)		# ADC1 is GPIO 32 (32-39)


# global variables


# setup
pot = ADC(Pin(POT_PIN, Pin.IN))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

# Loop
while True:
    pot_value = pot.read()				#range 0-4095
    pot_value_65535 = pot.read_u16() 	# range 0-65535
    microV_value = pot.read_uv()		#read an analog value in microvolt
    print ("ADC=",pot_value, " ADC=",pot_value_65535, " microVolt=",microV_value)
    sleep (1)
