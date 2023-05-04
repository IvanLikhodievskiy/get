import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]


def adc():
    x = 0

    for i in range(7, -1, -1):
        x += 2**i
        GPIO.output(dac, dec2bin(x))
        time.sleep(0.01)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            x -= 2**i

    return x


def led_num(x):
    num = dec2bin(x)
    GPIO.output(leds, num)


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

try:
    vals = []
    start_time = time.time()
    # GPIO.output(troyka, 1)
    x = adc()
    vals.append(3.3 * x / 256)
    led_num(x)

    while x < 225:
        x = adc()
        vals.append(3.3 * x / 256)
        led_num(x)

    GPIO.output(troyka, 1)
    x = adc()
    vals.append(3.3 * x / 256)
    led_num(x)

    while x > 60:
        x = adc()
        vals.append(3.3 * x / 256)
        led_num(x)

    finish_time = time.time()
    duration = finish_time - start_time

    plt.plot(vals)
    plt.show()

    vals_str = map(str, vals)

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(vals_str))

    print(duration)


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
