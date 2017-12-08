# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pins = [ 18 ,23 ,24 ,25 ,12 ,16 ,20 ,21 ,26 ,19 ] # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
for pin in pins:
    GPIO.setup(int(pin), GPIO.OUT) # LED pin set as output
    GPIO.output(int(pin), GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        for pin in pins:
            GPIO.output(int(pin), GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(int(pin), GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO