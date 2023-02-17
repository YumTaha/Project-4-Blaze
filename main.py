#!/usr/bin/env python3

from Movement.sounds import beep
from Movement.drive import drive_back, drive_straight, turn_degree
from Movement.error import error

#ALL VARIABLES THAT YOU CAN CHANGE
distance_cm = 40       # \
speed = 20          #  |=> YOU CAN CHANGE THESE VARIABLES
laps = 3            # /
degrees = 180       #/

# SUBTASK 1A
def subtask1A():#________________________DO NOT TOUCH_____________________________
  
    pos_straight, pos_negative = [], [] #________________________DO NOT TOUCH_____________________________

    for i in range(laps):
        print("\nLap ", i+1)

        # Drive forward .. cm at ..% speed
        pos1 = drive_straight(distance_cm, speed) #get the date for the Ys 
        print("Required forward distance (mm): ", distance_cm*10)
        print("Traveled distance (mm): {:.1f}".format(pos1))
        pos_straight.append(pos1)

        # Drive reverse .. cm at ..% speed
        pos2 = drive_back(distance_cm, speed) #get the date for the Ys 
        print("Required return distance (mm): ", -distance_cm*10)
        print("Return distance (mm): {:.1f}".format(pos2))
        pos_negative.append(pos2)

    #predict final position
    error(laps, pos_straight, pos_negative)

    
# SUBTASK 1B
def subtask1B():#________________________DO NOT TOUCH_____________________________
    drive_straight(distance_cm, speed)
    for i in range(laps):
        turn_degree(degrees-1, speed)
        drive_straight(distance_cm-1, speed)
    turn_degree(degrees-1, speed)


if __name__ == "__main__":#________________________REMOVE/ADD THE (#) TO ENABLE/DISABLE A TASK_____________________________

    beep()

    #subtask1A() #SUBTASK 1A 
    subtask1B() #SUBTASK 1B

    beep()
    pass
