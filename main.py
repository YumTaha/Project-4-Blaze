#!/usr/bin/env python3

#from Movement.coordinates import *
from Movement.sounds import beep, speaker, finished
from Movement.drive import drive_back, drive_straight
from Movement.error import error

def main():
    distance = 30 # \
    speed = 10    #  |=> YOU CAN CHANGE THESE VARIABLES
    laps = 2      # /
  
    pos_straight, pos_negative = [], [] #________________________DO NOT TOUCH_____________________________

    speaker()
    beep()
    for i in range(laps):
        print("\nLap ", i+1)
        # Drive forward .. cm at ..% speed
        #drive_straight(distance, speed)
        pos1 = drive_straight(distance, speed) #get the date for the Ys 
        print("Required forward distance (mm): ", distance*10)
        print("Traveled distance (mm): {:.1f}", pos1)
        pos_straight.append(pos1)
        # Drive reverse .. cm at ..% speed
        #drive_back(distance, speed)
        pos2 = drive_back(distance, speed) #get the date for the Ys 
        print("Required return distance (mm): ", -distance*10)
        print("Return distance (mm): {:.1f}", pos2)
        pos_negative.append(pos2)

    #predict final position
    error(laps, pos_straight, pos_negative)
    finished()
    

if __name__ == "__main__":#________________________DO NOT TOUCH_____________________________
    main()
