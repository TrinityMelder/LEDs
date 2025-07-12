import board
import neopixel
import time

NUM_LEDS = 16
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)


surprise_color = (76, 76, 76)

while True:
    
    for i in range(NUM_LEDS):
        pixels[i] = surprise_color
        pixels.show()
        time.sleep(0.07)

    time.sleep(0.3)

 
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.1)


    pixels.fill(surprise_color)
    pixels.show()
    time.sleep(0.15)

   
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.5)
