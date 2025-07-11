import board
import neopixel
import time

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

while True:
    # Build-up: one by one
    for i in range(NUM_LEDS):
        pixels[i] = (255, 255, 255)
        pixels.show()
        time.sleep(0.07)  # Slower buildup

    # Pause for tension
    time.sleep(0.3)

    # Flash burst: all off then sudden white
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.1)

    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(0.15)

    # Rapid decay
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.5)
