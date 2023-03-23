import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

GPIO.output(14, GPIO.input(15))
time.sleep(10)
GPIO.output(14, GPIO.input(15))
time.sleep(10)
GPIO.output(14, GPIO.input(15))
time.sleep(10)

GPIO.cleanup(14)
GPIO.cleanup(15)
