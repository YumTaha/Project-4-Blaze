def error(laps, distance, pos_on, pos_back):
    import random

    # Position tracker
    x = random.uniform(-1,1)
    finalY = 0 # Initialize the position

    if len(pos_on) == 0:
        pos_on = [0] * len(pos_back)
    if len(pos_back) == 0:
        pos_back = [0] * len(pos_on)

    for i in range(len(pos_on)):

        # Checking for a 0 all values list
        if pos_on[i] == 0:
            pos_on[i] = distance
        if pos_back[i] == 0:
            pos_back[i] = -distance

        # Add the error to the position
        finalY += pos_on[i] + pos_back[i]

    # Print the final position
    print("\n\nFinal position: x = {:.2f} cm, y = {:.2f} cm".format(x, (finalY / 10)))
    print("Number of turns: {}".format(laps * 2))

'''
def calibrator(degrees):

    # Calibrate the degrees
    if degrees == 360:
        degrees = 355
    elif degrees == -360:
        degrees = -355
    elif degrees == 180:
        degrees = 177.5
    elif degrees == -180:
        degrees = -177.5
    elif degrees == 90:
        degrees = 88.75
    elif degrees == -90:
        degrees = -88.75
    else:
        pass
    return degrees
'''