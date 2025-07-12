import board
import neopixel
import time
import random

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

# Dark purple (fear) at ~30% brightness
fear_color = (int(90 * 0.3), 0, int(130 * 0.3))  # (27, 0, 39)

def fear_flicker(color, flashes=12):
    for _ in range(flashes):
        pixels.fill((0, 0, 0))
        num_active = random.randint(1, 4)  # 1–4 LEDs flash randomly
        for _ in range(num_active):
            i = random.randint(0, NUM_LEDS - 1)
            pixels[i] = color
        pixels.show()
        time.sleep(random.uniform(0.03, 0.09))
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(random.uniform(0.02, 0.06))

while True:
    fear_flicker(fear_color)
    time.sleep(random.uniform(0.2, 0.5))  # Short pause between bursts
