from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.sensor.lego import GyroSensor
from time import sleep as wait

def turn(angle):
    gyro = GyroSensor(); gyro.reset()

    # Connect to the motors and set their speed and stop mode
    left_motor, right_motor = LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_D)

    speed = 30
    stop_mode = 'hold'

    # Determine the direction(CW or CCW)
    if angle > 0: left_speed = speed; right_speed = -speed
    else: left_speed = -speed; right_speed = speed

    # Calculate the target angle based on the current angle and the desired turn angle
    current_angle = gyro.angle
    target_angle = current_angle + angle

    # Turn the robot until it reaches the target angle
    while abs(gyro.angle - target_angle) > 1:
        # Calculate the error between the current angle and the target angle
        error = target_angle - gyro.angle

        # Calculate the correction speed using proportional control
        correction_speed = error * 1.5

        # Set the motor speeds based on the correction speed and the direction of the turn
        left_motor.run_forever(speed_sp=left_speed + correction_speed, stop_action=stop_mode)
        right_motor.run_forever(speed_sp=right_speed - correction_speed, stop_action=stop_mode)

        # give robot time to turn
        wait(0.01)

    # Stop the motors
    left_motor.stop(stop_action=stop_mode); right_motor.stop(stop_action=stop_mode)
