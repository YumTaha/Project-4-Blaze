import ev3dev2.motor as motor
import ev3dev2.sensor.lego as sensor
from func.lift import lift_object
from time import sleep as wait

DISTANCE_OF_APPROACH_IN = 2.6

left_motor = motor.LargeMotor('outA')
right_motor = motor.LargeMotor('outD')
gyro_sensor = sensor.GyroSensor('in1')
ultrasonic_sensor = sensor.UltrasonicSensor('in3')

def drive_forward(distance_in_cm, OBJECT_ON_OFF, start='no'):
    if start == 'yes':
        mediumM = motor.MediumMotor(); mediumM.position = 0; wait(1)
        mediumM.on_for_degrees(-10, 56.75); mediumM.stop(); mediumM.off(); wait(1)

    left_motor.reset(); right_motor.reset(); gyro_sensor.reset()
    target_angle = 0; speed_in_cm_per_sec = 10

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
        if ultrasonic_sensor.distance_inches <= 6: speed_in_deg_per_sec -= 2
        if ultrasonic_sensor.distance_inches <= DISTANCE_OF_APPROACH_IN and OBJECT_ON_OFF:
            left_motor.off(brake=True); right_motor.off(brake=True)
            break

    actual_distance = (left_motor.position + right_motor.position) / 2 / 360 * (2 * 3.14 * 2.8)
    print('Distance need to traveled:', distance_in_cm)
    print('Actual distance traveled:', actual_distance)
    if OBJECT_ON_OFF: print('The obstacle is ', ultrasonic_sensor.distance_inches, ' inches forward.')

def slowly_approach():
    left_motor.reset(); right_motor.reset(); gyro_sensor.reset()
    target_angle = 0
    speed_in_cm_per_sec = 10

    speed_in_deg_per_sec = speed_in_cm_per_sec / (2 * 3.14 * 2.8) * 360
    degrees_to_turn = 50 / (2 * 3.14 * 2.8) * 360

    left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)
    right_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)

    while left_motor.is_running or right_motor.is_running:
        current_angle = gyro_sensor.angle
        error = current_angle - target_angle
        correction_factor = error / 10
        left_motor.speed_sp = speed_in_deg_per_sec + correction_factor
        right_motor.speed_sp = speed_in_deg_per_sec - correction_factor

        if ultrasonic_sensor.distance_inches <= 1.3:
                    left_motor.off(brake=True); right_motor.off(brake=True)
                    break
    
    actual_distance = (left_motor.position + right_motor.position) / 2 / 360 * (2 * 3.14 * 2.8)

    print('Actual approach distance:', actual_distance)
    
    left_motor.reset(); gyro_sensor.reset()
    wait(2)
    lift_object()