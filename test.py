import pygame
import RPi.GPIO as GPIO
import time
import os

#global input

def UpdateTimer():
    global actualTime
    global startTime
    global showedTime
    global startPauseTime
    global pauseTime
    global TimerState

    
    actualTime = time.time()

    if (ButtonState == "Release" or ButtonState == "Released" or ButtonState == "Push"):
        if TimerState == "initial":
            showedTime = 300
        elif TimerState == "started":
            showedTime = actualTime - startTime - pauseTime 
        elif TimerState == "pause":
            pauseTime += actualTime - startPauseTime
            showedTime = actualTime - startTime - pauseTime
        elif TimerState == "finish":
            showedTime = 0
            pauseTime = 0
            #alarm
        else:
            print("error")
            
    elif ButtonState == "Pushed":
        print("test")
        if TimerState == "initial":
            startTime = time.time()
            TimerState = "started"
        elif TimerState == "started":
            startPauseTime = time.time()
            pauseTime += actualTime - startPauseTime
            TimerState = "pause"   
        elif TimerState == "pause":
            TimerState = "started"  
        else:
            print("error")



def UpdateButton():
    global PreviousState
    global PushTick
    global ButtonState
    global ResetTrigger
    global screen
    global font
    global cycle
    input = GPIO.input(buttonPin)
    
    if input != PreviousState:
        PreviousState = input
        
        if input == 0:
            ButtonState = "Pushed"
            PushTick = time.perf_counter()
            
        else:
            ResetTrigger = 0
            ButtonState = "Released"
            PushDuration = time.perf_counter() - PushTick
    else:
        if PreviousState == 0:
            ButtonState = "Push"
            PushDuration = time.perf_counter() - PushTick
            #vérifier etat du chrono
                
            if (PushDuration > 2) and (ResetTrigger == 0):
                ResetTrigger = 1
                ButtonState = "Pushed2Second"
                #reset chrono
        else:
            ButtonState = "Release"
    #print(ButtonState)
    

buttonPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
PreviousButtonState = 1
PreviousState = 1
PushTick = 0
cycle = 0
ButtonState = "Release"
ResetTrigger = 0
TimerState = "initial"
showedTime = 300
startTime = 0
pauseTime = 0
pauseStartTime = 0
actualTime = 0
while True:
    UpdateButton()
    UpdateTimer()
    print(showedTime)
    
    '''
    print(pauseTime)
    print(pauseStartTime)
    print(actualTime)
    '''
    time.sleep(0.5)
    
    
