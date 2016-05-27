#print in terminal when button is pressed

import RPi.GPIO as GPIO
import time

buttonPin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input = GPIO.input(buttonPin)

while True:
    
    input_state = GPIO.input(buttonPin)
    
    if input_state == False: 
        print("Button Pressed")
        time.sleep(0.5)

