def error(laps, distance, pos_on=[], pos_back=[]):
    import random

    # Position tracker
    x = random.uniform(-1,1)
    finalY = 0 # Initialize the position

    # Initialize pos_on and pos_back as empty lists if not provided
    if len(pos_on) == 0:
        pos_on = []
    if len(pos_back) == 0:
        pos_back = []

    for i in range(len(pos_on)):

        # Checking for a 0 all values list
        if pos_on[i] == 0:
            pos_on[i] = distance
        if pos_back[i] == 0:
            pos_back[i] = -distance

        # Add the error to the position
        finalY += pos_on[i] - pos_back[i]

    # Print the final position
    print("\n\nFinal position: x = {:.2f} cm, y = {:.2f} cm".format(x, (finalY / 10)))
    print("Number of turns: {}".format(laps * 2))
