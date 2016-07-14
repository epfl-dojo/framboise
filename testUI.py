import pygame
import RPi.GPIO as GPIO
import time
import os
from pygame.locals import *
from pygame import mixer

def mainLoop():
    UpdateButton()
    UpdateTimer()
    #print(showedTime)
    #print(minutes)
    #print(seconds)
    print(output_string)
    #print("-------------")
    #print(TimerState)
    #time.sleep(0.2)

def UpdateTimer():
    global actualTime
    global startTime
    global showedTime
    global TimerState
    global totalTime
    global minutes
    global seconds
    global output_string
    global screen
    global font
    global text

    actualTime = round(time.time())
    screen.fill(BLACK)

    if (ButtonState == "Release" or ButtonState == "Released" or ButtonState == "Push"):
        if TimerState == "initial":
            showedTime = 300
        elif TimerState == "started":
            showedTime = totalTime -(actualTime - startTime)
        elif TimerState == "pause":
            showedTime = showedTime
        elif TimerState == "finish":
            print("finish")
            showedTime = 0
            startTime = 0
            actualTime = 0
            totalTime = 300
            alert.play()
            time.sleep(1)     
        else:
            print("error 1")
            
    elif ButtonState == "Pushed":
        
        if TimerState == "initial":
            startTime = round(time.time())
            TimerState = "started"
        elif TimerState == "started":
            startPauseTime = round(time.time())
            totalTime = showedTime
            TimerState = "pause"   
        elif TimerState == "pause":
            startTime = round(time.time())
            showedTime = totalTime -(actualTime - startTime)
            TimerState = "started"
        elif TimerState == "finish":
            TimerState = "initial"
        else:
            print("error 2")

    elif ButtonState == "Pushed2Second":
        TimerState = "initial"
        showedTime = 300
        startTime = 0
        actualTime = 0
        totalTime = 300
    else:
        print("error 3")

    if showedTime == 0:
        TimerState = "finish"

    minutes = showedTime // 60
    seconds = showedTime % 60
    output_string = "{0:02}:{1:02}".format(round(minutes-0.4), round(seconds-0.4))
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [100, 100])
    pygame.display.flip()

def UpdateButton():
    global PreviousState
    global PushTick
    global ButtonState
    global ResetTrigger
    
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
                
            if (PushDuration > 2) and (ResetTrigger == 0):
                ResetTrigger = 1
                ButtonState = "Pushed2Second"
        else:
            ButtonState = "Release"
            
mixer.init()
alert = mixer.Sound('beep-01a.wav')

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("Timer")
font = pygame.font.Font(None, 50)

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
showedTime = 5
startTime = 0
actualTime = 0
totalTime = 5

while True:
    mainLoop()


    
    
