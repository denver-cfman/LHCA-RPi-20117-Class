# External module imports
import RPi.GPIO as GPIO
import time
import random

# Pin Definitons:
pins = [ 18 ,23 ,24 ,25 ,12 ,16 ,20 ,21 ,26 ,19 ] # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
for pin in pins:
    GPIO.setup(int(pin), GPIO.OUT) # LED pin set as output
    GPIO.output(int(pin), GPIO.LOW) # Make sure to "turn off" the LED as the start state.

""" This is what a function looks like.
It has 2 inputs:
inPin  this is an intiger representing the BCM pin number to turn on then off again ...  ( Default is 18 )
inTime this is the amount of time to wait between "On" and "Off" state ...  ( Default is 0.075 seconds ... )
"""
def light(inPin = 18, inTime = 0.075):
    GPIO.output(int(inPin), GPIO.HIGH)
    time.sleep(inTime)
    GPIO.output(int(inPin), GPIO.LOW)

def justRed(inTime = 0.075):
    redLights = [21, 19]
    GPIO.output(int(redLights[0]), GPIO.HIGH)
    GPIO.output(int(redLights[1]), GPIO.HIGH)
    time.sleep(inTime)
    GPIO.output(int(redLights[0]), GPIO.LOW)
    GPIO.output(int(redLights[1]), GPIO.LOW)

def justGreen(inTime = 0.075):
    greenLights = [20, 26]
    GPIO.output(int(greenLights[0]), GPIO.HIGH)
    GPIO.output(int(greenLights[1]), GPIO.HIGH)
    time.sleep(inTime)
    GPIO.output(int(greenLights[0]), GPIO.LOW)
    GPIO.output(int(greenLights[1]), GPIO.LOW)

def justYellow(inTime = 0.075):
    yellowLights = [18 ,23 ,24 ,25 ,12 ,16]
    for y in yellowLights:
        GPIO.output(int(y), GPIO.HIGH)
        time.sleep(inTime)
        GPIO.output(int(y), GPIO.LOW)

print("Here are the Red Lights")
justRed(long("1"))

print("Here are the Green Lights")
justGreen(long("1"))

print("Here are the Yellow Lights")
justYellow(long("1"))

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        foo=int(random.randint(0, (len(pins)-1)))
        light(inPin=int(pins[int(foo)]), inTime=float("0.75"))

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO