#!/usr/bin/env python3

from Movement.reader import read_barcode, read_black, box
from time import sleep, time
from ev3dev2.sound import Sound
from Movement.drive import turn_degree, drive
from ev3dev2.motor import MediumMotor, OUTPUT_B
from time import sleep

'''THIS IS WHERE I CHECK THE VURNABILITY OF EACH FUNCTION AND HOW WELL THEY WORK'''


def lift_hand(duration, direction='up'):
    # Create an instance of the medium motor
    motor = MediumMotor(OUTPUT_B)

    # Set the initial speed and acceleration values
    initial_speed = 0
    acceleration = 10  # speed increase per second

    # Determine the target speed based on the direction
    target_speed = 50 if direction == 'up' else -50

    # Set the motor speed and run the motor for the specified duration
    motor.on(initial_speed)
    start_time = time()
    while (time() - start_time) < duration:
        current_speed = motor.speed
        if current_speed != target_speed:
            # Gradually increase/decrease the motor speed
            if direction == 'up':
                new_speed = min(current_speed + acceleration, target_speed)
            else:
                new_speed = max(current_speed - acceleration, target_speed)
            motor.on(new_speed)
        else:
            # Motor has reached the target speed, continue running at that speed
            motor.on(target_speed)

    # Stop the motor and disconnect
    motor.off()
    motor.stop_action = 'coast'
    motor.reset()
    motor = None

def main():
    lift_hand(5, 'up')


if __name__ == '__main__':
    main()




