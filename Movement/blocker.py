from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from math import pi


# Initialize some global variables 
wheel_diameter_mm = 56
wheel_circumference_mm = pi * wheel_diameter_mm

for port in [INPUT_1, INPUT_2, INPUT_3, INPUT_4]:
    try:
        gyro = GyroSensor(port)
        gyro.reset()
        gyro_angle_initial = gyro.angle
    except:
        pass
for port in [INPUT_1, INPUT_2, INPUT_3, INPUT_4]:
    try:
        ultra = UltrasonicSensor(port)
    except:
        pass


def stopper(distance_cm, speed, direction='forward'):

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
    walker = True

    # Loop until the robot has traveled the target distance
    while walker:

        # checking for osbtacles
        if 0: 
            walker = False

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
