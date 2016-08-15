import pygame
import RPi.GPIO as GPIO
import time
import os

global PushDuration
global PreviousState
global input
global ButtonState

PreviousState = 1
ButtonState = "Release"

def UpdateButton(PreviousState):
    buttonPin = 21
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input = GPIO.input(buttonPin)

    if input != PreviousState:
        if input == 0:
            ButtonState = "Pushed"
            PushDuration = time.process_time()
        else:
            ButtonState = "Released"
        PreviousState = input
    else:
        if PreviousState == 0:
            ButtonState = "Push"
        else:
            ButtonState = "Release"

while True:
    UpdateButton(PreviousState)
    print(ButtonState)    
    
    
    

