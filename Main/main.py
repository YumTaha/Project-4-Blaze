#!/usr/bin/env python3
#This is the main file for blaze to work
from Movement.move import * #move_forward, move_backward, turn_left, turn_right, stop (THE FIRST ONES TAKE 3 ARGUMENTS (LEFT SPEED AND RIGHT SPEED and distance))
from Movement.position import * #get_position (takes 1 ARGUMENT)
from Movement.error import * #error
from time import sleep



def main():
    while True:
        distance = input("What is the distance Y ? ").lower()
        if distance.isnumeric():
            distance = int(distance)
            break
    while True:
        laps = input("how many laps? ").lower()
        if laps.isnumeric():
            laps = int(laps)
            break
    
    for n in range(laps):
        print(f"\n\nLap {laps}:")
        move_forward(50, 50, distance) #2 arguments (left and right speeds)
        sleep(2)
        position = get_position(distance)
        print(f"Current position: x={position[0]}, y={position[1]}")
        move_backward(50, 50, distance) #2 arguments (left and right speeds)
        sleep(2)
        position = get_position(distance)
        print(f"Current position: x={position[0]}, y={position[1]}")
    stop()
    sleep(2)

    error(laps) #output the error
    
    
# Call the main function
if __name__ == "__main__":
    main()

