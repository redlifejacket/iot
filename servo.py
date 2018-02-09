#!/usr/bin/python3
# Shyam Govardhan
# 10 February 2018
# Coursera: Interfacing with the Raspberry Pi
# Week 4 Assignment

import time
import RPi.GPIO as GPIO

LED_PIN = 12           # Board Pin 12
FREQUENCY = 50         # in Hertz
DC_MIN = 0             # Minimum Duty Cycle
DC_MAX = 100           # Maximum Duty Cycle
SLEEP_INTERVAL = 0.1   # Seconds
SPEED = 15             # Step interval

def changeLedBrightness(comment, startDc, endDc, stepDc):
  global SLEEP_INTERVAL
  for dc in range(startDc, endDc, stepDc):
    pwm.ChangeDutyCycle(dc)
    print(comment, dc)
    time.sleep(SLEEP_INTERVAL)

# Main program
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, FREQUENCY)
pwm.start(DC_MIN)

try:
  while True:
    changeLedBrightness("Brightening up  ", DC_MIN, DC_MAX, SPEED)
    changeLedBrightness("Dimming down    ", DC_MAX, DC_MIN - 1, SPEED * -1)
except KeyboardInterrupt:
  pass

pwm.stop()
GPIO.cleanup()
