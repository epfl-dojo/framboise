import pygame
import RPi.GPIO as GPIO
import time
import os

def test():
    buttonPin = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    input = GPIO.input(buttonPin)

    while True:
    
        input_state = GPIO.input(buttonPin)
    
        if input_state == False: 
            timer();
            time.sleep(0.5)
    return

def timer():
    
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
        start_time = 3
         
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
        
    	return

test();

