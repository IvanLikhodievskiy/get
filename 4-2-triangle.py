import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    print("Set period in seconds")
    s = float(input())
    t = s / 512
    while True:
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(t)
        for i in range(255, 0, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(t)


except KeyboardInterrupt:
    print("The program has stoppped clicking on a key")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()