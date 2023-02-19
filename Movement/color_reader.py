from ev3dev2.sensor.lego import ColorSensor, TouchSensor

def read_barcode():
    # Create a ColorSensor and TouchSensor object
    sensor = ColorSensor()
    touch_sensor = TouchSensor()

    # Initialize an empty list to store the colors
    colors = []

    # Initialize a variable to keep track of the previous state of the touch sensor
    prev_touch_state = True

    # Read colors until the list has a length of 4
    while len(colors) < 4:
        # Get the current state of the touch sensor
        curr_touch_state = touch_sensor.is_pressed

        # If the touch sensor was previously released and is now pressed, read a new color
        if not prev_touch_state and curr_touch_state:
            # Get the current color detected by the sensor
            color = sensor.color

            # If the color is black, append 1 to the colors list
            if color == ColorSensor.COLOR_BLACK:
                colors.append(1)

            # If the color is white, append 0 to the colors list
            elif color == ColorSensor.COLOR_WHITE:
                colors.append(0)

        # Update the previous state of the touch sensor
        prev_touch_state = curr_touch_state

    # Return the list of colors
    return colors
