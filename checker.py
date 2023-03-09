#!/usr/bin/env python3

from Movement.reader import read_barcode, read_black, box
from time import sleep
from ev3dev2.sound import Sound
from Movement.drive import turn_degree, drive
from ev3dev2.motor import MediumMotor, OUTPUT_B
from time import sleep

'''THIS IS WHERE I CHECK THE VURNABILITY OF EACH FUNCTION AND HOW WELL THEY WORK'''

def lift_hand(duration=1):
    # Create an instance of the medium motor on output port A
    motor = MediumMotor(OUTPUT_B)

    # Set the motor speed and direction to lift the hand up
    motor.on_for_seconds(speed=50, seconds=duration)

    # Turn off the motor
    motor.off()

def main():
    inch = 5
    cm = inch * 2.54
    drive(cm, 30, direction="forward")


if __name__ == '__main__':
    main()




