#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from random import randrange

led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

led_pwm = GPIO.PWM(led_pin, 200)

led_pwm.start(100)

def brightness(new_brightness):
        global led_pwm
        led_pwm.ChangeDutyCycle(new_brightness)

def flicker():
	brightness(randrange(0, 100))
	time.sleep(randrange(1, 10) * 0.01)

while True:
        flicker()
