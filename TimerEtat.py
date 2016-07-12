import pygame
import RPi.GPIO as GPIO
import time
import os

#Déclaration des variables globales

#Bouton
global PreviousState
global PushTick
global ButtonState
global ResetTrigger
global screen
global font
global cycle
global buttonPin

#Chrono
global frame_count
global frame_rate
global start_time
global timer_state
global total_seconds
frame_count = 0
frame_rate = 60
start_time = 300
#total_seconds = 0
def UpdateButton():
    input = GPIO.input(buttonPin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    PreviousButtonState = 1
    PreviousState = 0
    PushTick = 0
    cycle = 0
    ButtonState = "Release"
    ResetTrigger = 0
    
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
    print(ButtonState)
            
    #if ButtonState == "Pushed":
    #    print("Start")
    #elif ButtonState == "Released":
    #    print("Stop")
        
    #cycle += 1
    #BLACK = (0, 0, 0)
    #WHITE = (255, 255, 255)
    #screen.fill(BLACK)
    # Blit to the screen
    #text = font.render("%d" % cycle, True, WHITE)
         
    #screen.blit(text, [100, 100])
            
    #Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()         

    #pygame.display.set_caption("Timer")

def UpdateChrono(frame_count, frame_rate, start_time):
    print(total_seconds)
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    print(total_seconds)
    time.sleep(10)
    
    '''
    if total_seconds < 0:
        total_seconds = 0
        os.popen("cvlc /home/pi/framboise/Alarm.mp3")
    '''
    
         
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
    # Calculate total seconds
    
    total_seconds = start_time - (frame_count // frame_rate)
    print(total_seconds)
    time.sleep(100)
         
    # Limit frames per second
    clock.tick(frame_rate)
         
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    print(total_seconds)
    if total_seconds==0:
        #timer_state = initial
        print("initial")
        
    elif (total_seconds > 0 and frame_count < 300):
        #timer_state = demarrer
        print("demarrer")

    elif total_seconds == 300:
        #timer_state = fini
        print("fini")
    else:
        print("ERROR")

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
            
buttonPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input = GPIO.input(buttonPin)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # Set the screen background
    screen.fill(BLACK)
    
    UpdateButton()
    UpdateChrono(frame_count, frame_rate, start_time)

pygame.quit()  

'''
#buttonPin = 21
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
 #Blit to the screen
text = font.render(" ", True, WHITE)
         
screen.blit(text, [100, 100])
            
#Go ahead and update the screen with what we've drawn.
pygame.display.flip()         

pygame.display.set_caption("Timer")

while True:
    Start = time.perf_counter()
    Elapsed = time.perf_counter() - Start;
    Sleep = 1/60 - Elapsed
    if Sleep > 0:
        time.sleep(Sleep)
    continue
    input_state = GPIO.input(buttonPin)

    
    if input_state == False: 
        time.sleep(0.5)

    
         #Define some colors
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
'''
