import RPi.GPIO as GPIO

class ShiftRegister:
    register_type = '74HC595'

    """
    data_pin => pin 14 on the 74HC595
    latch_pin => pin 12 on the 74HC595
    clock_pin => pin 11 on the 74HC595
    """
    def __init__(self, data_pin, latch_pin, clock_pin, numberOf595s=1):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin

        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)

        self.outputs = [GPIO.LOW] * (8*numberOf595s)
        # DEBUG
        print(self.outputs)

    """
    output_number => Value from 0 to 7 pointing to the output pin on the 74HC595
    0 => Q0 pin 15 on the 74HC595
    1 => Q1 pin 1 on the 74HC595
    2 => Q2 pin 2 on the 74HC595
    3 => Q3 pin 3 on the 74HC595
    4 => Q4 pin 4 on the 74HC595
    5 => Q5 pin 5 on the 74HC595
    6 => Q6 pin 6 on the 74HC595
    7 => Q7 pin 7 on the 74HC595

    value => a state to pass to the pin, could be HIGH or LOW
    """
    def setOutput(self, output_number, value):
        try:
            self.outputs[output_number] = value
        except IndexError:
            raise ValueError("Invalid output number. Can be only an int from 0 to " + len(self.outputs))

    def setOutputs(self, outputs):
        if len(self.outputs) != len(outputs):
            raise ValueError("setOutputs must be an array with " + len(self.outputs) + " elements")

        self.outputs = outputs

    def latch(self):
        GPIO.output(self.latch_pin, GPIO.LOW)

        for i in range(len(self.outputs)-1, -1, -1):
            print (self.outputs[i], end='')
            print (",", end='')
            GPIO.output(self.clock_pin, GPIO.LOW)
            GPIO.output(self.data_pin, self.outputs[i])
            GPIO.output(self.clock_pin, GPIO.HIGH)
        print ("")

        GPIO.output(self.latch_pin, GPIO.HIGH)
