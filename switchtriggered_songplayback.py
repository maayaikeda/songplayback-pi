# before starting, install all packages needed from terminal
# pygame
# also type in terminal to set audio output to head jacket (amixer cset numid=3 1)

# import raspberry pi gpio library
import RPi.GPIO as GPIO

# need this for delay
import time

# need this for time stamps
from datetime import datetime

# need this for audio playback
import pygame

# file to write the trigger times
outfile = open("test_output.txt", 'w')

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)
# Set pin 10 (GPIO18)
# to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create empty list
button_pressed_raw = []
button_pressed = []
press_count = 0

# initialize mixer module
pygame.mixer.init()
# set output file
tutorsong = "O402_song.wav"
s = pygame.mixer.Sound(tutorsong)


while press_count<20: # quit after 20 times
    if GPIO.input(10) == GPIO.HIGH:
        s.play()
        # add counts
        press_count += 1
        print("Song was played back" + str(press_count) + " times.  "
              + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # add delay so that it is only played once/key peck
        time.sleep(0.2)
        # append on list
        button_pressed_raw.append(datetime.now())
        button_pressed.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


print(button_pressed)
# print(button_pressed_raw)
# use above only if you're interested in raw time stamps


# write triggered times in text file line by line        
for line in button_pressed:
    outfile.write(line)
    outfile.write("\n")
outfile.close()
