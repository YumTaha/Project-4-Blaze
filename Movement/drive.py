from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from math import pi

# Search for the gyro and reset it to zero
for port in [INPUT_1, INPUT_2, INPUT_3, INPUT_4]:
    try:
        gyro = GyroSensor(port)
        gyro.reset()
        gyro_angle_initial = gyro.angle
    except:
        pass

# Function to calibrate angle measurements
def calibrator(degrees):
    adjustments = {360: 350, 180: 175, 90: 86.5} # Dictionary of adjustments for each degree (Robot is not perfect)
    return adjustments.get(degrees, degrees) # Return the calibrated degree, or the original degree if no calibration is necessary

# Initialize some global variables 
wheel_diameter_mm = 56
wheel_circumference_mm = pi * wheel_diameter_mm

#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..

def drive(distance_cm, speed, direction='forward'):

    """
    Make the robot drive straight for a certain distance at a given speed.
    :param distance_cm: The distance to travel in centimeters
    :param speed: The speed to travel at, in degrees per second
    :param direction: The direction to drive in, either 'forward' or 'backward'
    :return: The distance the robot actually traveled in millimeters
    """
    # Get the global variables
    global gyro_angle_initial
    global wheel_diameter_mm
    global wheel_circumference_mm
    gyro = GyroSensor(INPUT_1)
    gyro.reset()
    # Convert the target distance from centimeters to millimeters
    target_distance_mm = distance_cm * 10

    # Calculate the number of wheel rotations needed to travel the target distance
    if direction == 'forward':
        rotations = target_distance_mm / wheel_circumference_mm
    elif direction == 'backward':
        rotations = -target_distance_mm / wheel_circumference_mm
    else:
        raise ValueError("Invalid direction. Must be either 'forward' or 'backward'")

    # Get references to the left and right motors
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)

    # Reset the motor positions
    left_motor.reset()
    right_motor.reset()

    # Initialize the left and right motor speeds to be the same
    left_speed = speed
    right_speed = speed

    # Loop until the robot has traveled the target distance
    while True:
        # Get the current angle of the gyro and adjust the motor speeds accordingly
        angle = gyro.angle - gyro_angle_initial

        if abs(angle) > 1:
            if angle > 0:
                left_speed = speed * 0.9 if direction == 'forward' else speed * 1.1
                right_speed = speed * 1.1 if direction == 'forward' else speed * 0.9
            else:
                left_speed = speed * 1.1 if direction == 'forward' else speed * 0.9
                right_speed = speed * 0.9 if direction == 'forward' else speed * 1.1
        else:
            left_speed = speed
            right_speed = speed

        # Move the robot forward or backward using both motors at the adjusted speeds
        left_motor.on_for_rotations(left_speed, rotations, block=False)
        right_motor.on_for_rotations(right_speed, rotations, block=False)

        # Check if the robot has traveled the target distance and stop the motors if it has
        average_rotation_mm = (left_motor.rotations + right_motor.rotations) / 2
        if abs(average_rotation_mm) >= abs(rotations):
            left_motor.off(brake=True)
            right_motor.off(brake=True)

            # Exit the while loop
            break

    # Return the actual distance traveled in millimeters
    return (left_motor.rotations * pi * wheel_diameter_mm) if direction == 'forward' else (-left_motor.rotations * pi * wheel_diameter_mm)


#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..

def turn_degree(degrees, speed, direction='right'):
    # Global variable to store the initial angle reading from the gyro
    global gyro_angle_initial

    # Slowing down the speed
    speed_turn = int(speed / 4)


    #calibrating the degrees
    result  = calibrator(degrees)
    print(result)

    # Set the mode of the gyro sensor to measure rate
    gyro.mode = gyro.modes[1]

    # Create instances of the left and right motors
    left_motor, right_motor = LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_D)

    # Reset the motor tachometers to 0
    left_motor.reset()
    right_motor.reset()

    # Determine the direction and speed for each motor
    if result > 0:
        # If the turn is to the left, set the left motor speed to negative and the right motor speed to positive
        if direction == 'right':
            left_speed = speed_turn
            right_speed = -speed_turn
        elif direction == 'left':
            left_speed = -speed_turn
            right_speed = speed_turn

    # Loop until the robot has turned the specified number of degrees
    while True:
        # Calculate the current angle of the robot by subtracting the initial angle from the gyro reading
        angle = gyro.angle - gyro_angle_initial

        # Check if the robot has turned the desired number of degrees
        if abs(angle - result) > 1:
            # If not, determine the direction to turn based on the current angle and the target angle
            if angle > result:
                # If the robot has turned too far, adjust the motor speeds to turn in the opposite direction
                left_speed = -speed_turn if direction == 'right' else speed_turn
                right_speed = speed_turn if direction == 'right' else -speed_turn
            else:
                # If the robot has turned too far, adjust the motor speeds to turn in the opposite direction
                left_speed = speed_turn if direction == 'right' else -speed_turn
                right_speed = -speed_turn if direction == 'right' else speed_turn

            # Set the motor speeds to turn the robot
            left_motor.on(speed=left_speed)
            right_motor.on(speed=right_speed)
        else:
            # If the robot has turned the desired number of degrees, reset the gyro sensor and stop the motors
            gyro.reset()
            left_motor.off(brake=True)
            right_motor.off(brake=True)

            # Exit the while loop
            break
