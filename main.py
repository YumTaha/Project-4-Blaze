#!/usr/bin/env python3

#run command (brickrun -r ./Project-4-Blaze-/Main/main.py)
#This is the main file for blaze to work

from Movement.move import * #move_forward, move_backward, turn_left, turn_right, stop (THE FIRST ONES TAKE 3 ARGUMENTS (LEFT SPEED AND RIGHT SPEED and distance))
from Movement.error import * #error
from Movement.sounds import *
from Movement.coordinates import *
from time import sleep

distance = int(input("Y? "))
speed = int(input("speed? "))
laps = int(input("Laps? "))
wheel = Wheel(diameter_mm=68.8, width_mm=36)
rotations_for_mm = distance / wheel.circumference_mm

speaker()

for n in range(1, laps+1):
    
    print("\nLap " + str(n) + ":")
    move_forward(speed, speed, rotations_for_mm) 
    move_backward(speed, speed, rotations_for_mm) 
    
clean_up()
sleep(2)

error(laps, distance) #output the error


