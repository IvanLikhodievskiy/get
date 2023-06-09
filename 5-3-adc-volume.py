import RPi.GPIO as GPIO
import time
from math import ceil

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

def adc():
    x = 0

    for i in range(7, -1, -1):
        x += 2**i
        GPIO.output(dac, dec2bin(x))
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            x -= 2**i

    return x

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        x = ceil(adc()/32)
        signal = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(x):
            signal[7-i] = 1
        GPIO.output(leds, signal)

except KeyboardInterrupt:
    print("The program has been stopped by pressing on a key")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()