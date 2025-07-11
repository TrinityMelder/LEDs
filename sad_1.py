import board
import neopixel
import time
import math

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

base_color = (0, 0, 180)  # Slightly dimmer blue to feel sadder

def slow_fade(color, steps=80, delay=0.05):
    while True:
        # Fade in
        for i in range(steps):
            brightness = math.sin(i / steps * math.pi)  # Smooth in and out
            scaled_color = tuple(int(c * brightness) for c in color)
            pixels.fill(scaled_color)
            pixels.show()
            time.sleep(delay)

slow_fade(base_color)
