import pygame
import RPi.GPIO as GPIO
import time
import os

def Update():
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
            if (PushDuration > 2) and (ResetTrigger == 0):
                ResetTrigger = 1
                ButtonState = "Pushed2Second"
        else:
            ButtonState = "Release"
    #print(ButtonState)
    if ButtonState == "Pushed":
        print("Start")
    elif ButtonState == "Released":
        print("Stop")
        

    cycle += 1
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(BLACK)
    # Blit to the screen
    text = font.render("%d" % cycle, True, WHITE)
         
    screen.blit(text, [100, 100])
            
    #Go ahead and update the screen with what we've drawn.
    pygame.display.flip()         

    pygame.display.set_caption("Timer")
        
            
buttonPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
PreviousButtonState = 1
PreviousState = 0
PushTick = 0
cycle = 0
ButtonState = "Release"
ResetTrigger = 0    
pygame.init()
         
# Set the height and width of the screen
size = [300, 200]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 50)
screen.fill(BLACK)
# Blit to the screen
text = font.render("Hello", True, WHITE)
         
screen.blit(text, [100, 100])
            
#Go ahead and update the screen with what we've drawn.
pygame.display.flip()         

pygame.display.set_caption("Timer")
while True:
    Start = time.perf_counter()
    Update()
    Elapsed = time.perf_counter() - Start;
    Sleep = 1/60 - Elapsed
    #print(Sleep)
    if Sleep > 0:
        time.sleep(Sleep)
    continue
    input_state = GPIO.input(buttonPin)

    
    if input_state == False: 
        time.sleep(0.5)

    
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
         
        pygame.init()
         
        # Set the height and width of the screen
        size = [300, 200]
        screen = pygame.display.set_mode(size)
         

        pygame.display.set_caption("Timer")
         
        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
         
        font = pygame.font.Font(None, 50)
         
        frame_count = 0
        frame_rate = 60
        start_time = 300         
        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
          
            # Set the screen background
            screen.fill(BLACK)
         
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
         
            # Calculate total seconds
            total_seconds = start_time - (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
                os.popen("cvlc /home/pi/Alarm.mp3")
         
            # Divide by 60 to get total minutes
            minutes = total_seconds // 60
         
            # Use modulus (remainder) to get seconds
            seconds = total_seconds % 60
         
            # Use python string formatting to format in leading zeros
            output_string = "{0:02}:{1:02}".format(minutes, seconds)
            
         
            # Blit to the screen
            text = font.render(output_string, True, WHITE)
         
            screen.blit(text, [100, 100])
         
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            frame_count += 1
            
         
            # Limit frames per second
            clock.tick(frame_rate)
            
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()