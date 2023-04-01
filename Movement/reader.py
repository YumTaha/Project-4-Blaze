from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MediumMotor, OUTPUT_B
from time import time
from Movement.errors import remove_none

@remove_none
def lift_reader():
    # Create an instance of the medium motor on port B
    motor = MediumMotor('outB', speed=10)
    combination = []
    duration = 2

    # Set the motor speed and run the motor for the specified amount of time
    motor.on()
    start_time = time()
    while (time() - start_time) < duration:
        key = read_barcode()
        combination.append(key)

    motor.stop()

    return combination


def read_barcode():
    # Create a ColorSensor object
    color_sensor = ColorSensor()

    # Read colors for 0.1 seconds, 40 times (4 combinations of 4 digits)
        # Get the current color detected by the sensor
    color = color_sensor.color

    # If the color is black, append 1 to the current combination
    if color == ColorSensor.COLOR_BLACK:
            print('black')
            return 1

    # If the color is white, append 0 to the current combination
    elif color == ColorSensor.COLOR_WHITE:
            print('white')
            return 0
    
def read_black():
    # Create instances of the ColorSensor and TouchSensor classes
    sensor = ColorSensor()
    
    # Loop forever
        
        # Read the percentage of reflected light intensity from the color sensor
    perc = sensor.reflected_light_intensity
    
    # If the percentage is less than 9, return 5
    if perc < 9:
        return 0
    
    # If the percentage is less than 40, return 1
    elif perc < 40:
        return 1

    
       
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
