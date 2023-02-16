#!/usr/bin/env python3
# Import ev3 libraries
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.wheel import *
# Set up the motors for controlling the robot

motor = MoveTank(OUTPUT_A, OUTPUT_D)


# Define the functions for moving the robot
def move_forward(speedL, speedR, rotations_for_mm):
    motor.on_for_rotations(SpeedPercent(speedL), SpeedPercent(speedR), rotations_for_mm)
    motor.stop(stop_action="coast") 


def move_backward(speedL, speedR, rotations_for_mm):
    motor.on_for_rotations(-SpeedPercent(speedL), -SpeedPercent(speedR), rotations_for_mm)
    motor.stop(stop_action="coast") 

def turn_left(speedL, speedR, rotations_for_mm):
    motor.on_for_rotations(-SpeedPercent(speedL), SpeedPercent(speedR), rotations_for_mm)
    motor.stop(stop_action="coast") 

def turn_right(speedL, speedR, rotations_for_mm):
    motor.on_for_rotations(SpeedPercent(speedL), -SpeedPercent(speedR), rotations_for_mm)
    motor.stop(stop_action="coast")


# stop and clean everything after motor stops
def clean_up():
    motor.off()
    motor.off()
