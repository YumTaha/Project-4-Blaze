#!/usr/bin/env python3

from Movement.lifter import lift_hand
from Movement.reader import lift_reader
from time import sleep, time
from ev3dev2.motor import MediumMotor, OUTPUT_B

'''THIS IS WHERE I CHECK THE VURNABILITY OF EACH FUNCTION AND HOW WELL THEY WORK'''


def lift(speed, time):
    # Create an instance of the medium motor on port A
    motor = MediumMotor(OUTPUT_B)


    # Set the motor speed and run the motor for the specified amount of time
    motor.on_for_seconds(speed=-speed, seconds=time)
    motor.off()
    
# Call the lift function to lift the handle for 4 seconds at 50% speed



def main():
    # print(dir(MediumMotor))
    # lift(speed=10, time=1)
    a = lift_reader()
    print(a)

if __name__ == '__main__':
    main()




