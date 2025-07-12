import board
import neopixel
import time
import math

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)


base_color = (0, 0, 255)
brightness_scale = 0.3  
sad_color = tuple(int(c * brightness_scale) for c in base_color)

def sadness_fade(color, steps=80, delay=0.05, pause=0.5):
    while True:
       
        for i in range(steps, -1, -1):
            brightness = i / steps  
            scaled_color = tuple(int(c * brightness) for c in color)
            pixels.fill(scaled_color)
            pixels.show()
            time.sleep(delay)
        
        time.sleep(pause)

sadness_fade(sad_color)
