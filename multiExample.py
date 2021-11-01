#!/usr/bin/python3

import RPi.GPIO as GPIO
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep

GPIO.setmode(GPIO.BOARD)


data_pin = 26 #pin 14 on the 75HC595
latch_pin = 24 #pin 12 on the 75HC595
clock_pin = 22 #pin 11 on the 75HC595

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin, 2)

def sendOut(val, t):
    global  shift_register
    
    shift_register.setOutputs(val)
    shift_register.latch()
    sleep(t)


try:
    shift_register.latch()
    sleep(1)
    while 1:

#        empty = [GPIO.LOW] * 16
#        sendOut(empty, 1)

        for v in [ GPIO.LOW, GPIO.HIGH ]:
            shift_register.setOutput(1, v)
            shift_register.setOutput(5, v)
            shift_register.setOutput(9, v)
            shift_register.setOutput(13, v)
            shift_register.latch()

            print(shift_register.outputs)

            sleep(10)
            print("Change")

        

except KeyboardInterrupt:
    print("Ctrl-C - quit")

GPIO.cleanup()
