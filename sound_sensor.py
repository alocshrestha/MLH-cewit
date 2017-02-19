#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)

def loop():
	while True:
		value = ADC.read(0)
		if value < 50:
			print value
		time.sleep(0.1)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass
