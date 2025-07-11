import board
import neopixel
import time

NUM_LEDS = 16
GROUP_SIZE = 4
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

blue = (0, 0, 255)
off = (0, 0, 0)

def bounce(color, group_size=GROUP_SIZE, delay=0.15):
    while True:
        # Forward
        for i in range(NUM_LEDS - group_size + 1):
            pixels.fill(off)
            for j in range(group_size):
                pixels[i + j] = color
            pixels.show()
            time.sleep(delay)
        # Backward
        for i in reversed(range(NUM_LEDS - group_size + 1)):
            pixels.fill(off)
            for j in range(group_size):
                pixels[i + j] = color
            pixels.show()
            time.sleep(delay)
