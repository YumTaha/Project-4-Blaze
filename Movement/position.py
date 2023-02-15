#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor

def get_position(distance):
    motor_A = LargeMotor(OUTPUT_A)
    motor_B = LargeMotor(OUTPUT_B)

    # Set the motor speed and run time based on the distance
    if distance > 0:
        speed = 360
        run_time = (distance / 20) * 1000
    else:
        speed = -360
        run_time = (-distance / 20) * 1000

    # Run the motors and wait for them to stop
    motor_A.on_for_seconds(speed=speed, seconds=run_time/1000)
    motor_B.on_for_seconds(speed=speed, seconds=run_time/1000)

    # Calculate the final position relative to the starting position
    final_x = 0
    final_y = distance

    return final_x, final_y
