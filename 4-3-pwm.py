import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)

try:
    while True:
        print("Please, enter fill coefficient")
        x = int(input())
        p.start(x)
        k = (x/100)*3.3
        print("The voltage is {0:.2f} volts".format(k))

finally:
    p.stop()
    GPIO.output(22, 0)
    GPIO.cleanup()