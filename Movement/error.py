#!/usr/bin/env python3

def error(n):
    import random

    #maximum travel distance (in cm) and N
    y = 150
    # position tracker
    x = 0 
    direction = 1 #because the first movement is forward

    for lap in range(int(n)):
        # foreward
        distance = y / 2
        distance += random.uniform(-20, 20) 
        x += distance * direction

        #reverse
        direction *= -1

        #backward
        distance = y / 2
        distance += random.uniform(-20, 20)
        x += distance * direction

    # Print the final position
    print(f"Final position: x = {x} cm")
    print(f"Number of turns: {int(n) * 2}")
