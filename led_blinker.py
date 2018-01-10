#!/usr/bin/python3
# Shyam Govardhan
# 6 December 2018
# Coursera: The Raspberry Pi Platform and Python Programming for the Raspberry Pi
# Module 4 Assignment

import time
import RPi.GPIO as GPIO
ledPin = 7
buttonPin = 8
BLINK_SPEED = .5

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.add_event_detect(buttonPin, GPIO.BOTH, callback=buttonCallback, bouncetime=200)
    print("GPIO Version:", GPIO.VERSION)

def blinkLed():
    print('Blinking LED')
    GPIO.output(ledPin,True)
    time.sleep(BLINK_SPEED)
    GPIO.output(ledPin,False)
    time.sleep(BLINK_SPEED)

def constantLed():
    print("Setting LED to constant")
    GPIO.output(ledPin,True)

def process():
    print("Executing process()")
    try:
        while True:
            if not GPIO.input(buttonPin):
                print("process(): Button pressed")
                constantLed()
            else:
                print("process(): Button released")
                blinkLed()
    except KeyboardInterrupt:  
        print("Interrupted by user (^C)... Cleaning up...")
        GPIO.cleanup()
        exit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        GPIO.cleanup()
    print("Done")

# Main Program
init()
process()
