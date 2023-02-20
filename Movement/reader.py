from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from time import sleep


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

            else:
                pass

        # Update the previous state of the touch sensor
        prev_touch_state = curr_touch_state

    # Return the list of colors
    return colors


def read_black():
    # Create instances of the ColorSensor and TouchSensor classes
    sensor = ColorSensor()
    touch_sensor = TouchSensor()
    
    # Loop forever
    while True:
        # Pause for 0.2 seconds
        sleep(0.2)
        
        # Read the percentage of reflected light intensity from the color sensor
        perc = sensor.reflected_light_intensity
        
        # If the percentage is less than 9, return 5
        if perc < 9:
            return 5
        
        # If the percentage is less than 40, return 1
        elif perc < 40:
            return 1
        
        # If the touch sensor is pressed, break out of the loop
        elif touch_sensor.is_pressed:
            break
        
        # If none of the above conditions 

        
        
def box():
    # Define a dictionary of box types, where each box type is represented by a list of 4 values.
    boxType = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}
    
    # Read the barcode (assuming read_barcode() returns a list of 4 values)
    barcode = read_barcode()
    
    # Loop over each box type in the dictionary
    for box_name in boxType:
        # Compare the values for the current box type to the barcode
        if boxType[box_name] == barcode:
            # If there is a match, return the name of the box type
            return box_name
    
    # If there is no match, return None
    return None
