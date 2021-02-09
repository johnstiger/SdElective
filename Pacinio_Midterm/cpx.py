
from adafruit_circuitplayground import cp
from time import sleep

cp.pixels.brightness = 1
a = 9
while True:
    for i in range(0,10):
        if a < 0:
            a = 9
        cp.pixels[a] = (255,255,255)
        sleep(0.5)
        cp.pixels[0] = (0,0,0)
        cp.pixels[5] = (0,0,0)

        if (a == 0 or a == 5):
            cp.pixels[a] = (255,255,255)
            a -=1
            continue
        cp.pixels[a] = (0,0,0)
        a -=1
