#!/usr/bin/env python3

def error(n, y):
    import random

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
    print("\nFinal position: x = {:.2f} cm, y = {:.2f} cm".format(x, y))
    print("Number of turns: {}".format(int(n) * 2))

