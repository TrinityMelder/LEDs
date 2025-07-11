import board
import neopixel
import time
import random

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

def flickering_snake(color, delay_range=(0.03, 0.07)):
    # Forward pass
    for i in range(NUM_LEDS):
        pixels.fill((0, 0, 0))
        pixels[i] = color
        pixels.show()
        time.sleep(random.uniform(*delay_range))
    # Reverse pass
    for i in reversed(range(NUM_LEDS)):
        pixels.fill((0, 0, 0))
        pixels[i] = color
        pixels.show()
        time.sleep(random.uniform(*delay_range))

while True:
    flickering_snake((90, 0, 130))  # Deep purple with jittery speed
    time.sleep(random.uniform(0.1, 0.3))  # Uneasy pauses
