#!/usr/bin/env python3
# Import ev3 libraries
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from time import sleep

# Set up the motors for controlling the robot
motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_C)

# Define the functions for moving the robot

def move_forward(speed=50):
    motor_left.on(speed)
    motor_right.on(speed)

def move_backward(speed=50):
    motor_left.on(-speed)
    motor_right.on(-speed)

def turn_left(speed=50):
    motor_left.on(-speed)
    motor_right.on(speed)

def turn_right(speed=50):
    motor_left.on(speed)
    motor_right.on(-speed)

def stop():
    motor_left.off()
    motor_right.off()

# Clean up the motors when the program exits
def clean_up():
    motor_left.off()
    motor_right
