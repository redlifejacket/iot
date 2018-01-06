#!/usr/bin/python3
# Shyam Govardhan
# 6 December 2018
# Coursera: The Raspberry Pi Platform and Python Programming for the Raspberry Pi
# Module 4 Assignment

import time
import RPi.GPIO as GPIO
ledPin = 7
buttonPin = 8
BLINK_SPEED = 1

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=buttonCallback, bouncetime=200)
    print("GPIO Version:", GPIO.VERSION)

def blinkLed():
    print('Blink Input was LOW')
    GPIO.output(ledPin,True)
    time.sleep(BLINK_SPEED)
    GPIO.output(ledPin,False)
    time.sleep(BLINK_SPEED)

def constantLed():
    print('Blink Input was HIGH')
    GPIO.output(ledPin,True)

def process():
    print("Executing blink()")
    while True:
        if GPIO.input(buttonPin):
            constantLed()
        else:
            blinkLed()
    print("Done")

def buttonCallback(channel):
    while True:
        if GPIO.input(buttonPin):
            constantLed()
        else:
            print('Input was LOW')
            process()

# Main Program
init()
process()
