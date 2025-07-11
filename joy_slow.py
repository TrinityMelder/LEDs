import board
import neopixel
import time
import math

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)
joy_color = (255, 255, 0)  # Bright yellow

def joy_pulse(color, steps=40, delay=0.015):
    while True:
        for i in range(steps):
            brightness = math.sin(i / steps * math.pi)
            scaled_color = tuple(int(c * brightness) for c in color)
            pixels.fill(scaled_color)
            pixels.show()
            time.sleep(delay)

joy_pulse(joy_color)
