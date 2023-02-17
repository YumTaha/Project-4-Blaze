#!/usr/bin/env python3

def error(laps, pos_on, pos_back):
    import random

    # position tracker
    x = random.uniform(-1,1)
    finalY = 0 #initialize the position

    for i in range(len(pos_on)):

        finalY += pos_on[i] + pos_back[i]


    # Print the final position
    print("\n\nFinal position: x = {:.2f} cm, y = {:.2f} cm".format(x, (finalY / 10)))
    print("Number of turns: {}".format(laps * 2))

