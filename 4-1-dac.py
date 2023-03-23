import RPi.GPIO as GPIO

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        print("If you want to light the lamps, please, enter a digit from 0 to 255. If you want to quit, please, press q")
        x = input()
        if x == 'q':
            break
        if not x[min(len(x) - 1, 1):].isdigit():
            print("You haven't input a number")
        elif x.find('.') != -1:
            print("You haven't input an integer")
        elif x[0] == "-":
            print("Your value is negative")
        elif int(x) > 255:
            print("Your value is too big")
        else:
            x = int(x)
            GPIO.output(dac, dec2bin(x))
            k = (x / 256) * 3.3
            print("The voltage is {0:.2f} volts".format(k))

except KeyboardInterrupt:
    print("The program has stoppped clicking on a key")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()