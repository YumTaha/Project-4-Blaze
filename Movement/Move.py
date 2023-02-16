#!/usr/bin/env python3
# Import ev3 libraries
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D
from time import sleep
# Set up the motors for controlling the robot
motor_left = LargeMotor(OUTPUT_A)
motor_right = LargeMotor(OUTPUT_D)

# Define the functions for moving the robot

def move_forward(speedL, speedR, distance):
    run_time = (distance / 20) * 1000
    motor_left.on_for_seconds(speedL=speedL, seconds=run_time/1000)
    motor_right.on_for_seconds(speedR=speedR, seconds=run_time/1000)


def move_backward(speedL, speedR, distance):
    run_time = (distance / 20) * 1000
    motor_left.on_for_seconds(speedL=-speedL, seconds=run_time/1000)
    motor_right.on_for_seconds(speedR=-speedR, seconds=run_time/1000)

def turn_left(speedL, speedR, distance):
    run_time = (distance / 20) * 1000
    motor_left.on_for_seconds(speedL=-speedL, seconds=run_time/1000)
    motor_right.on_for_seconds(speedR=speedR, seconds=run_time/1000)

def turn_right(speedL, speedR, distance):
    run_time = (distance / 20) * 1000
    motor_left.on_for_seconds(speedL=speedL, seconds=run_time/1000)
    motor_right.on_for_seconds(speedR=-speedR, seconds=run_time/1000)

def stop():
    motor_left.off()
    motor_right.off()

# stop and clean everything after motor stops
def clean_up():
    motor_left.off()
    motor_right
