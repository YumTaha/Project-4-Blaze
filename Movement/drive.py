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


# Initialize some global variables 
wheel_diameter_mm = 56
wheel_circumference_mm = pi * wheel_diameter_mm

#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..


def drive_straight(distance_cm, speed):
    """
    Make the robot drive straight for a certain distance at a given speed.
    :param distance_cm: The distance to travel in centimeters
    :param speed: The speed to travel at, in degrees per second
    :return: The distance the robot actually traveled in millimeters
    """
    # Get the global variables
    global gyro_angle_initial
    global wheel_diameter_mm
    global wheel_circumference_mm

    # Convert the target distance from centimeters to millimeters
    target_distance_mm = distance_cm * 10

    # Calculate the number of wheel rotations needed to travel the target distance
    rotations = target_distance_mm / wheel_circumference_mm

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
                left_speed = speed * 0.9
                right_speed = speed * 1.1
            else:
                left_speed = speed * 1.1
                right_speed = speed * 0.9
        else:
            left_speed = speed
            right_speed = speed

        # Move the robot forward using both motors at the adjusted speeds
        left_motor.on_for_rotations(left_speed, rotations, block=False)
        right_motor.on_for_rotations(right_speed, rotations, block=False)

        # Check if the robot has traveled the target distance and stop the motors if it has
        average_rotation_mm = (left_motor.rotations + right_motor.rotations) / 2
        if average_rotation_mm >= rotations:
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            break

    # Return the actual distance traveled in millimeters
    return (left_motor.rotations) * (pi * wheel_diameter_mm)

#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..


def drive_back(distance_cm, speed):
    """
    Make the robot drive straight backward for a certain distance at a given speed.
    :param distance_cm: The distance to travel in centimeters
    :param speed: The speed to travel at, in degrees per second
    :return: The distance the robot actually traveled in millimeters
    """

    # Get the global variables
    global gyro_angle_initial
    global wheel_diameter_mm
    global wheel_circumference_mm

    # Convert the target distance from centimeters to millimeters
    target_distance_mm = distance_cm * 10

    # Calculate the number of wheel rotations needed to travel the target distance
    rotations = -target_distance_mm / wheel_circumference_mm

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
                left_speed = speed * 1.1
                right_speed = speed * 0.9
            else:
                right_speed = speed * 1.1
                left_speed = speed * 0.9
        else:
            left_speed = speed
            right_speed = speed

        # Move the robot forward using both motors at the adjusted speeds
        left_motor.on_for_rotations(left_speed, rotations, block=False)
        right_motor.on_for_rotations(right_speed, rotations, block=False)

        # Check if the robot has traveled the target distance and stop the motors if it has
        average_rotation_mm = abs(left_motor.rotations + right_motor.rotations) / 2
        if average_rotation_mm >= abs(rotations):
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            
            # Exit the while loop
            break

    # Return the actual distance traveled in millimeters
    return (left_motor.rotations) * (pi * wheel_diameter_mm)
    

#....#####.....######.........#....#....######....######.........######....######....#....#....######....#....#..
#....#....#....#....#.........##...#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#....#....#....#.........#.#..#....#....#......##.............##......#....#....#....#....#.........######..
#....#....#....#....#.........#..#.#....#....#......##.............##......#....#....#....#....#.........#....#..
#....#####.....######.........#...##....######......##.............##......######....######....######....#....#..


def turn_degree(degrees, speed):
    # Global variable to store the initial angle reading from the gyro
    global gyro_angle_initial

    #slowing down the speed
    speed_turn = int(speed / 4)
    
    # Set the mode of the gyro sensor to measure rate
    gyro.mode = gyro.modes[1]

    # Create instances of the left and right motors
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)

    # Reset the motor tachometers to 0
    left_motor.reset()
    right_motor.reset()

    # Determine the direction and speed for each motor
    if degrees > 0:
        # If the turn is to the left, set the left motor speed to negative and the right motor speed to positive
        left_speed = -speed_turn
        right_speed = speed_turn
    else:
        # If the turn is to the right, set the left motor speed to positive and the right motor speed to negative
        left_speed = speed_turn
        right_speed = -speed_turn

    # Loop until the robot has turned the specified number of degrees
    while True:
        # Calculate the current angle of the robot by subtracting the initial angle from the gyro reading
        angle = gyro.angle - gyro_angle_initial
        print(angle)
        # Check if the robot has turned the desired number of degrees
        if abs(angle - degrees) > 1:
            # If not, determine the direction to turn based on the current angle and the target angle
            if angle > degrees:
                # If the robot has turned too far to the left, adjust the motor speeds to turn to the right
                left_speed = -speed_turn
                right_speed = speed_turn
            else:
                # If the robot has turned too far to the right, adjust the motor speeds to turn to the left
                left_speed = speed_turn
                right_speed = -speed_turn

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
    