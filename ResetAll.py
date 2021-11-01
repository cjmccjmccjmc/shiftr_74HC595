#!/usr/bin/python3

import RPi.GPIO as GPIO
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep

GPIO.setmode(GPIO.BOARD)

data_pin = 26 #pin 14 on the 75HC595
latch_pin = 24 #pin 12 on the 75HC595
clock_pin = 22 #pin 11 on the 75HC595

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin)

GPIO.cleanup()
