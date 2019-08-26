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
active = 1
count = 0
new_button = 1
x0 = 14
i2c = io.I2C(board.SCL, board.SDA)
t_display = adafruit_ht16k33.segments.Seg14x4(i2c, address=0x71)
# b_display = adafruit_ht16k33.segments.Seg14x4(i2c, address=0x72)
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

# Timer Start    
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


timer_start()
reset_leds(BLACK)
t_display.print(count)
t_display.show()
# b_display.print(count)
# b_display.show()

while True:
    while active == 1:
    #    t_display.print(timer)
    #    t_display.show()
    #    time.sleep(1)
    #    timer = timer - 1
    # choose random LED
        if new_button == 1:
            x = random_led(num_pixels)
            print("x is %d" % x)
            print("x0 is %d" % x0)
            while x0 == x:
                x = random_led(num_pixels)
                print("x0, x were equal - new random")
            reset_leds(BLACK)
            b_leds[x] = WHITE
            print("LED #%d Lit" % x)
            b_leds.show()
            new_button = 0
            x0 = x
    # monitor button presses
        for button in buttons:
            if not button.value:  # pressed?
                i = buttons.index(button)
                print("Button #%d Pressed" % i)
                if i == x:
                    count = count + 1
                    print("Count is %d" % count)
                    t_display.print('    ')
                    t_display.print(count)
                    t_display.show()
                    new_button = 1
        if timer == -1:
            t_display.print('TIME')
            t_display.show()
            active = 0

    # i = buttons.index(button)
    # print("Button #%d Pressed" % i)
    # if i == x:
    #    count = count + 1
    #    new_button = 1
    
    
# TO DO
# - Timer Service
# - Switch Manifold
# - Configurable - Timer
# - Reaction Time Algorithm
# - 
