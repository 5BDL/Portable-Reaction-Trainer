import board
import busio as io
import digitalio
import adafruit_ht16k33.segments
import time
import neopixel
import random

NPIN = board.A0
LED_SPEED = 1.0
num_pixels = 12
# Timer will be selectable in the future
timer = 30
i2c = io.I2C(board.SCL, board.SDA)
t_display = adafruit_ht16k33.segments.Seg14x4(i2c, address=0x71)
b_display = adafruit_ht16k33.segments.Seg14x4(i2c, address=0x72)
# Button LED controller
b_leds = neopixel.NeoPixel(NPIN, num_pixels, brightness=10, auto_write=False)
# Button Switch definition
buttonpins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, 
              board.D6, board.D7, board.D8, board.D9, board.D10, board.D11]

# Array of buttons
buttons = []

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

for pin in buttonpins:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)
    
# Random LED Function
def random_led(b):
    return (random.randint(0, b-1))
    
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
    t_display.print('5BDL')
    t_display.show()
    time.sleep(3)

    t_display.print('    ')
    t_display.print('RDY')
    t_display.show()
    time.sleep(2)
    t_display.print('    ')
    t_display.print('SET')
    time.sleep(2)
    t_display.print('    ')
    t_display.print('GO')
    time.sleep(1)

# def countdown(tc):
#    display.print(tc)
#    display.show()
#    time.sleep(1)
#    tc = tc - 1
#    if tc == -1:
#        display.print('TIME')
#        display.show()

timer_start()

while timer > -1:
    t_display.print(timer)
    t_display.show()
    time.sleep(1)
    timer = timer - 1
    if timer == -1:
        t_display.print('TIME')
        t_display.show()
        
    b_display.print(timer+1)
    b_display.show()
    reset_leds(BLACK)
    # choose random LED
    x = random_led(num_pixels)
    b_leds[x] = WHITE
    b_leds.show()
    print("random LED")
    
    for button in buttons:
        if not button.value:  # pressed?
            i = buttons.index(button)
 
            print("Button #%d Pressed" % i)
    
    
# TO DO
# - Timer Service
# - Switch Manifold
# - Configurable - Timer
# - Reaction Time Algorithm
# - 
    
    
