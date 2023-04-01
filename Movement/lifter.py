#!/usr/bin/env python3
from time import sleep, time
from ev3dev2.motor import MediumMotor, OUTPUT_B


def lift_hand(duration, direction='up'):
    # Create an instance of the medium motor
    motor = MediumMotor(OUTPUT_B)

    # Set the initial speed and acceleration values
    initial_speed = 0
    acceleration = 1  # speed increase per second

    # Determine the target speed based on the direction
    target_speed = -10 if direction == 'up' else 10

    # Set the motor speed and run the motor for the specified duration
    motor.on(initial_speed)
    start_time = time()
    while (time() - start_time) < duration:
        current_speed = motor.speed
        if current_speed != target_speed:
            # Gradually increase/decrease the motor speed
            if direction == 'down':
                new_speed = min(current_speed + acceleration, target_speed)
            else:
                new_speed = max(current_speed - acceleration, target_speed)
            motor.on(new_speed)
        else:
            # Motor has reached the target speed, continue running at that speed
            motor.on(target_speed)

    # Stop the motor and disconnect
    motor.off()
