import pygame
import RPi.GPIO as GPIO
import time
import os


def UpdateTimer():
    global actualTime
    global startTime
    global showedTime
    global TimerState
    global totalTime

    actualTime = time.time()

    if (ButtonState == "Release" or ButtonState == "Released" or ButtonState == "Push"):
        if TimerState == "initial":
            showedTime = 10
        elif TimerState == "started":
            showedTime = totalTime -(actualTime - startTime)
        elif TimerState == "pause":
            showedTime = showedTime                    
        else:
            print("error")
            
    elif ButtonState == "Pushed":
        
        if TimerState == "initial":
            startTime = time.time()
            TimerState = "started"
        elif TimerState == "started":
            startPauseTime = time.time()
            totalTime = showedTime
            TimerState = "pause"   
        elif TimerState == "pause":
            startTime = time.time()
            showedTime = totalTime -(actualTime - startTime)
            TimerState = "started"  
        else:
            print("error")

    elif ButtonState == "Pushed2Second":
        TimerState = "initial"
        showedTime = 300
        startTime = 0
        actualTime = 0
        totalTime = 300


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
        300
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
                
            if (PushDuration > 2) and (ResetTrigger == 0):
                ResetTrigger = 1
                ButtonState = "Pushed2Second"
        else:
            ButtonState = "Release"

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
showedTime = 10
startTime = 0
actualTime = 0
totalTime = 10
while showedTime > 0:
    UpdateButton()
    UpdateTimer()
    print(showedTime)
    time.sleep(0.5)
    
#os.popen("cvlc /home/pi/framboise/Alarm.mp3")
print("alarm")
showedTime = 10
startTime = 0
actualTime = 0
totalTime = 10
    
    
