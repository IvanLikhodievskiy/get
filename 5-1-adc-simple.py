import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            return i

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        voltage = ((adc() / 256) * 3.3)
        print(voltage)

except KeyboardInterrupt:
    print("The program has been stopped by pressing on a key")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()