import board
import neopixel
import time
import random

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

def disgusting_flicker():
    while True:
        pixels.fill((0, 0, 0))  # All off first
        num_on = random.randint(2, 8)  # Random # of LEDs to turn on

        for _ in range(num_on):
            led = random.randint(0, NUM_LEDS - 1)
            green_intensity = random.choice([50, 100, 180, 255])  # Vary intensity
            pixels[led] = (0, green_intensity, 0)

        pixels.show()
        time.sleep(random.uniform(0.15, 0.5))  # Slightly slower, irregular flicker

disgusting_flicker()
