import ev3dev2.motor as motor
import ev3dev2.sensor.lego as sensor
from func.lift import lift_object
from time import sleep as wait
LEFT_WHEEL_PORT = 'outA'
RIGHT_WHEEL_PORT = 'outD'
GYRO_PORT = 'in1'
ULTRASONIC_PORT = 'in3'
DISTANCE_OF_APPROACH_IN = 2.5

left_motor = motor.LargeMotor(LEFT_WHEEL_PORT)
right_motor = motor.LargeMotor(RIGHT_WHEEL_PORT)
gyro_sensor = sensor.GyroSensor(GYRO_PORT)
ultrasonic_sensor = sensor.UltrasonicSensor(ULTRASONIC_PORT)

def drive_forward(distance_in_cm, OBJECT_ON_OFF):
    left_motor.reset()
    gyro_sensor.reset()
    target_angle = 0
    speed_in_cm_per_sec = 10

    speed_in_deg_per_sec = speed_in_cm_per_sec / (2 * 3.14 * 2.8) * 360
    degrees_to_turn = distance_in_cm / (2 * 3.14 * 2.8) * 360

    left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)
    right_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)

    while left_motor.is_running or right_motor.is_running:
        current_angle = gyro_sensor.angle
        error = current_angle - target_angle
        correction_factor = error / 10
        left_motor.speed_sp = speed_in_deg_per_sec + correction_factor
        right_motor.speed_sp = speed_in_deg_per_sec - correction_factor

        if ultrasonic_sensor.distance_inches <= 2.5 and OBJECT_ON_OFF:
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            break

    actual_distance = (left_motor.position + right_motor.position) / 2 / 360 * (2 * 3.14 * 2.8)
    print('Distance need to traveled:', distance_in_cm)
    print('Actual distance traveled:', actual_distance)
    if OBJECT_ON_OFF: print('The obstacle is ', ultrasonic_sensor.distance_inches, ' inches forward.')

def slowly_approach():
    left_motor.reset()
    gyro_sensor.reset()
    target_angle = 0
    speed_in_cm_per_sec = 10

    speed_in_deg_per_sec = speed_in_cm_per_sec / (2 * 3.14 * 2.8) * 360
    degrees_to_turn = DISTANCE_OF_APPROACH_IN / (2 * 3.14 * 2.8) * 360

    left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)
    right_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)

    while left_motor.is_running or right_motor.is_running:
        current_angle = gyro_sensor.angle
        error = current_angle - target_angle
        correction_factor = error / 10
        left_motor.speed_sp = speed_in_deg_per_sec + correction_factor
        right_motor.speed_sp = speed_in_deg_per_sec - correction_factor

        if ultrasonic_sensor.distance_centimeters <= .1:
                    left_motor.off(brake=True)
                    right_motor.off(brake=True)
                    break
    
    actual_distance = (left_motor.position + right_motor.position) / 2 / 360 * (2 * 3.14 * 2.8)

    print('Imaginary approach distance:', DISTANCE_OF_APPROACH_IN)
    print('Actual approach distance:', actual_distance)
    
    wait(2)
    lift_object()