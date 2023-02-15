#!/usr/bin/env python3
#This is the main file for blaze to work
from Movement.move import * #move_forward, move_backward, turn_left, turn_right, stop
from Movement.position import * #get_position
from Movement.error import *
from time import sleep

while True:
    distance = input("What is the position? ").lower()
    if distance.isnumeric():
        distance = int(distance)
        break
def main():
    move_forward()
    sleep(2)
    position = get_position(distance)
    print(f"Current position: x={position[0]}, y={position[1]}")
    turn_left()
    sleep(1)
    move_forward()
    sleep(2)
    position = get_position(distance)
    print(f"Current position: x={position[0]}, y={position[1]}")
    turn_right()
    sleep(1)
    move_backward()
    sleep(2)
    stop()


# Call the main function
if __name__ == "__main__":
    main()

