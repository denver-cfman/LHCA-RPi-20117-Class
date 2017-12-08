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
    GPIO.output(int(pin), GPIO.LOW)

def light(inPin = 18, inTime = 0.075):
    GPIO.output(int(inPin), GPIO.HIGH)
    time.sleep(inTime)
    GPIO.output(int(inPin), GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        foo=int(random.randint(0, (len(pins)+1)))
        light(inPin=foo, inTime=float("0.075"))

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO