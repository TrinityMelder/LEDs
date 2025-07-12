import board
import neopixel
import time

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)


base_color = (255, 0, 0)
brightness_scale = 0.3
anger_color = tuple(int(c * brightness_scale) for c in base_color)

def anger_blink(color, blink_times=5, on_time=0.04, off_time=0.03):
    for _ in range(blink_times):
        pixels.fill(color)
        pixels.show()
        time.sleep(on_time)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(off_time)

while True:
    anger_blink(anger_color, blink_times=6)
    time.sleep(0.15)  
