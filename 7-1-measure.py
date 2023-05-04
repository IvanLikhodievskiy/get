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
    # initial values
    vals = []
    start_time = time.time()
    # Charging
    x = adc()
    vals.append(x)
    led_num(x)

    while x < 225:
        x = adc()
        vals.append(x)
        led_num(x)

    # Uncharging
    GPIO.output(troyka, 1)
    x = adc()
    vals.append(x)
    led_num(x)

    while x > 60:
        x = adc()
        vals.append(x)
        led_num(x)

    # Measuring time
    finish_time = time.time()
    duration = finish_time - start_time

    # Building a graph

    plt.plot(vals)
    plt.show()

    vals_str = map(str, vals)

    # Writing to files
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(vals_str))
    with open("settings.txt", "w") as outfile:
        outfile.write(str(duration))
        outfile.write(str(3.3/256))

    # Printing some parameters
    print("Время эксперимента", duration)
    print("Период одного измерения", 0.01)
    n = len(vals) - 1
    summ = 0
    for i in range(n):
        summ += abs(vals[i + 1] - vals[i])
    print("Средняя частота дискретизации", summ / (len(vals) - 1))
    print("Шаг квантования", 3.3 / 256)


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
