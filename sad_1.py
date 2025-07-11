import board
import neopixel
import time
import math

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)
sad_color = (0, 0, 180)  

def sadness_fade(color, steps=50, delay=0.035):
    while True:
        for i in range(steps):
            brightness = math.sin(i / steps * math.pi)
            scaled_color = tuple(int(c * brightness) for c in color)
            pixels.fill(scaled_color)
            pixels.show()
            time.sleep(delay)

sadness_fade(sad_color)
