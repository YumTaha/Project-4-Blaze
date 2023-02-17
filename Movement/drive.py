from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2
from math import pi

#gyro reset
gyro = GyroSensor(INPUT_2)
gyro.reset()
gyro_angle_initial = gyro.angle


def drive_straight(distance_cm, speed): #___________________DRIVE STRAIGHT_______________________
    global gyro_angle_initial

    wheel_diameter_mm = 68.9
    wheel_circumference_mm = pi * wheel_diameter_mm
    target_distance_mm = distance_cm * 10  # convert cm to mm
    rotations = target_distance_mm / wheel_circumference_mm

    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)



    left_motor.reset()
    right_motor.reset()

    left_speed = speed
    right_speed = speed
    
    while True:
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

        left_motor.on_for_rotations(left_speed, rotations, block=False)
        right_motor.on_for_rotations(right_speed, rotations, block=False)


        average_rotation_mm = (left_motor.rotations + right_motor.rotations) / 2
        if average_rotation_mm >= rotations:
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            break


    return (left_motor.rotations) * (pi * wheel_diameter_mm)

def drive_back(distance_cm, speed): #___________________DRIVE REVERSE_______________________
    global gyro_angle_initial

    wheel_diameter_mm = 68.9
    wheel_circumference_mm = pi * wheel_diameter_mm
    target_distance_mm = distance_cm * 10  # convert cm to mm
    rotations = -target_distance_mm / wheel_circumference_mm

    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)

    left_motor.reset()
    right_motor.reset()

    left_speed = speed
    right_speed = speed

    while True:
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

        left_motor.on_for_rotations(left_speed, rotations, block=False)
        right_motor.on_for_rotations(right_speed, rotations, block=False)


        average_rotation_mm = abs(left_motor.rotations + right_motor.rotations) / 2
        if average_rotation_mm >= abs(rotations):
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            break

    return (left_motor.rotations) * (pi * wheel_diameter_mm)
    
def turn_degree(degrees, speed): #___________________TURN_______________________
    global gyro_angle_initial

    gyro.mode = gyro.modes[1]

    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)

    left_motor.reset()
    right_motor.reset()

    if degrees > 0:
        left_speed = -speed
        right_speed = speed
    else:
        left_speed = speed
        right_speed = -speed

    while True:
        angle = gyro.angle - gyro_angle_initial

        if abs(angle - degrees) > 1:
            if angle > degrees:
                left_speed = -speed
                right_speed = speed
            else:
                left_speed = speed
                right_speed = -speed

            left_motor.on(speed=left_speed)
            right_motor.on(speed=right_speed)
        else:
            gyro.reset()
            left_motor.off(brake=True)
            right_motor.off(brake=True)


            break
