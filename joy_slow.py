import board
import neopixel
import time

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)


base_color = (255, 255, 0)
brightness_scale = 0.3
joy_color = tuple(int(c * brightness_scale) for c in base_color)

trail_length = 4
delay = 0.08

def joy_snake(color, loops=2):
    total_steps = NUM_LEDS * loops
    for step in range(total_steps):
        pixels.fill((0, 0, 0))  

        for i in range(trail_length):
            index = (step - i) % NUM_LEDS
            intensity = (trail_length - i) / trail_length
            faded_color = tuple(int(c * intensity) for c in color)
            pixels[index] = faded_color

        pixels.show()
        time.sleep(delay)

def joy_blink(color, blink_times=2, blink_delay=0.2):
    for _ in range(blink_times):
        pixels.fill(color)
        pixels.show()
        time.sleep(blink_delay)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(blink_delay)


while True:
    joy_snake(joy_color, loops=2)
    joy_blink(joy_color, blink_times=2)

