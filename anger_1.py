import board
import neopixel
import time
import random

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

def anger_burst():
    # Full strip flashes with jolting red
    for _ in range(3):
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(0.05)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.03)

    # Rapid chasing pulse
    for _ in range(2):
        for i in range(NUM_LEDS):
            pixels.fill((0, 0, 0))
            pixels[i] = (255, 0, 0)
            pixels.show()
            time.sleep(0.02)
        for i in reversed(range(NUM_LEDS)):
            pixels.fill((0, 0, 0))
            pixels[i] = (255, 0, 0)
            pixels.show()
            time.sleep(0.02)

while True:
    anger_burst()
    time.sleep(0.1)  # Short, tense break between bursts
