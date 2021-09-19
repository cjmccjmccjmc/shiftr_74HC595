#!/usr/bin/python3

import RPi.GPIO as GPIO
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep

GPIO.setmode(GPIO.BOARD)



data_pin = 22 #pin 14 on the 75HC595
latch_pin = 24 #pin 12 on the 75HC595
clock_pin = 26 #pin 11 on the 75HC595

NUMBER_OF_CHIPS = 2
UPPER_COUNT = NUMBER_OF_CHIPS * 8

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin, NUMBER_OF_CHIPS)



def allOffOn():
    for i in range(0, UPPER_COUNT):
        shift_register.setOutput(i, GPIO.LOW)
    shift_register.latch()
        
    sleep(1)
    print("Next")
    
    for i in range(0, UPPER_COUNT):
        shift_register.setOutput(i, GPIO.HIGH)
    shift_register.latch()
        
    sleep(1)
        
    # Set some output individually
    print("Next")
    

def OffOn(i):
    shift_register.setOutput(i, GPIO.LOW)
    shift_register.latch()
        
    sleep(1)
    print("Next")
    
    shift_register.setOutput(i, GPIO.HIGH)
    shift_register.latch()
        
    sleep(1)
        
    # Set some output individually
    print("Next")
    
def subs(val):

    for x in val:
        shift_register.setOutput(x, GPIO.LOW)
    shift_register.latch()
        
    sleep(1)
    print("Next")
    
    for x in val:
        shift_register.setOutput(x, GPIO.HIGH)
    shift_register.latch()
        
    sleep(1)
        
    # Set some output individually
    print("Next")


try:
    for i in range(0, UPPER_COUNT):
        shift_register.setOutput(i, GPIO.HIGH)
    shift_register.latch()
    while 1:
        allOffOn()


except KeyboardInterrupt:
    print("Ctrl-C - quit")

GPIO.cleanup()
