#!/usr/bin/env python3
#This is the main file for blaze to work
from Movement.Move import move_forward, move_backward, turn_left, turn_right, stop
from Movement.position import get_position
from time import sleep


def main():
    move_forward()
    sleep(2)
    position = get_position()
    print(f"Current position: x={position[0]}, y={position[1]}, angle={position[2]}")
    turn_left()
    sleep(1)
    move_forward()
    sleep(2)
    position = get_position()
    print(f"Current position: x={position[0]}, y={position[1]}, angle={position[2]}")
    turn_right()
    sleep(1)
    move_backward()
    sleep(2)
    stop()


# Call the main function
if __name__ == "__main__":
    main()

