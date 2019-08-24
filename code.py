import board
import busio as io
import adafruit_ht16k33.segments
import time
import neopixel
import random

NPIN = board.A1
LED_SPEED = 1.0
num_pixels = 12
# Timer will be selectable in the future
timer = 30
i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg14x4(i2c)
b_leds = neopixel.NeoPixel(NPIN, num_pixels, brightness=1, auto_write=False)

BLACK = (0, 0, 0)
WHITE = (255, 0, 0)

# Random LED Function
def random_led(b):
    return (random.randint(0,b-1))
    
# LED Reset to clear
def reset_leds(col):
    print("LED Reset")
    b_leds.fill(col)
    
# display[0] = 'F'
# display[1] = 'I'
# display[2] = 'D'
# display[3] = 'O'
# display.show()

# Adafruit_AlphaNum4 alpha4 = Adafruit_AlphaNum4()

# alpha4.begin(0x70)

# alpha4.writeDigitRaw(3, 0x0)

# alpha4.writeDigitRaw(0, 0x3FFF)

def timer_start():
    display.print('5BDL')
    display.show()
    time.sleep(3)

    display.print('    ')
    display.print('RDY')
    display.show()
    time.sleep(2)
    display.print('    ')
    display.print('SET')
    time.sleep(2)
    display.print('    ')
    display.print('GO')
    time.sleep(1)

#def countdown(tc):
#    display.print(tc)
#    display.show()
#    time.sleep(1)
#    tc = tc - 1
#    if tc == -1:
#        display.print('TIME')
#        display.show()

timer_start()

while timer > -1:
    display.print(timer)
    display.show()
    time.sleep(1)
    timer = timer - 1
    if timer == -1:
        display.print('TIME')
        display.show()
        
    reset_leds(BLACK)
    # choose random LED
    x = random_led(num_pixels)
    b_leds[x]=WHITE
    b_leds.show()
    
    
