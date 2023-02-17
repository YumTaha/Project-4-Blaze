#!/usr/bin/env python3

from Movement.sounds import beep, speaker, finished
from Movement.drive import drive_back, drive_straight, turn_degree
from Movement.error import error

#ALL VARIABLES THAT YOU CAN CHANGE
distance = 40       # \
speed = 10          #  |=> YOU CAN CHANGE THESE VARIABLES
laps = 3            # /
degrees = 180       #/

# SUBTASK 1A
def subtask1A():#________________________DO NOT TOUCH_____________________________
  
    pos_straight, pos_negative = [], [] #________________________DO NOT TOUCH_____________________________

    speaker()
    beep()
    for i in range(laps):
        print("\nLap ", i+1)

        # Drive forward .. cm at ..% speed
        pos1 = drive_straight(distance, speed) #get the date for the Ys 
        print("Required forward distance (mm): ", distance*10)
        print("Traveled distance (mm): {:.1f}", pos1)
        pos_straight.append(pos1)

        # Drive reverse .. cm at ..% speed
        pos2 = drive_back(distance, speed) #get the date for the Ys 
        print("Required return distance (mm): ", -distance*10)
        print("Return distance (mm): {:.1f}", pos2)
        pos_negative.append(pos2)

    #predict final position
    error(laps, pos_straight, pos_negative)
    finished()
    
# SUBTASK 1B
def subtask1B():#________________________DO NOT TOUCH_____________________________
    beep()
    drive_straight(distance, speed)
    for i in range(laps):
        turn_degree(degrees-1, speed)
        drive_straight(distance, speed)
    turn_degree(degrees-1, speed)


if __name__ == "__main__":#________________________REMOVE/ADD THE (#) TO ENABLE/DISABLE A TASK_____________________________
    speaker()
    beep()
    #subtask1A()
    #subtask1B()
    beep()
    pass
