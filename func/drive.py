import ev3dev2.motor as motor
import ev3dev2.sensor.lego as sensor
from func.lift import *
from time import sleep as wait

DISTANCE_OF_APPROACH_IN = 2.6
LIFTING_OF_START = 56.6
left_motor = motor.LargeMotor('outA')
right_motor = motor.LargeMotor('outD')
gyro_sensor = sensor.GyroSensor('in1')
ultrasonic_sensor = sensor.UltrasonicSensor('in3')

def pid_control(target_angle, current_angle, prev_error, integral, kp, ki, kd):
    error = target_angle - current_angle
    integral += error
    derivative = error - prev_error
    correction = kp * error + ki * integral + kd * derivative
    prev_error = error
    return correction, prev_error, integral

def drive(distance_in_cm, OBJECT_ON_OFF, start='no'):
    if start == 'yes':
        mediumM = motor.MediumMotor(); mediumM.position = 0; wait(1)
        mediumM.on_for_degrees(-10, LIFTING_OF_START); mediumM.stop(); mediumM.off(); wait(1)

    left_motor.reset(); right_motor.reset(); gyro_sensor.reset()
    gyro_sensor.mode = 'GYRO-RATE'  # set mode to GYRO-RATE to reset the angle to 0
    gyro_sensor.mode = 'GYRO-ANG'
    ultrasonic_sensor.mode = 'US-DIST-IN'; ultrasonic_sensor.value(0)
    target_angle = 0; speed_in_cm_per_sec = 10

    speed_in_deg_per_sec = speed_in_cm_per_sec / (2 * 3.14 * 2.8) * 360
    degrees_to_turn = distance_in_cm / (2 * 3.14 * 2.8) * 360

    # PID constants
    kp = 0.5
    ki = 0.01
    kd = 0.1
    prev_error = 0
    integral = 0

    left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)
    right_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)

    while abs(left_motor.position) < abs(degrees_to_turn) or abs(right_motor.position) < abs(degrees_to_turn):
        
        current_angle = gyro_sensor.angle
        correction_factor, prev_error, integral = pid_control(target_angle, current_angle, prev_error, integral, kp, ki, kd)
        correction_factor *= 1  # amplify the correction to make it stronger
        left_motor.speed_sp = (speed_in_deg_per_sec + correction_factor)
        right_motor.speed_sp = (speed_in_deg_per_sec - correction_factor)
        left_motor.run_forever()
        right_motor.run_forever()

        # print(((correction_factor, current_angle), (right_motor.speed_sp, left_motor.speed_sp)))

        if ultrasonic_sensor.distance_inches <= DISTANCE_OF_APPROACH_IN and OBJECT_ON_OFF:
            left_motor.stop(stop_action='hold')
            right_motor.stop(stop_action='hold')
            break

    left_motor.reset()
    right_motor.reset()
    gyro_sensor.reset()


# def slowly_approach():
#     left_motor.reset(); right_motor.reset(); gyro_sensor.reset()
#     target_angle = 0
#     speed_in_cm_per_sec = 10

#     speed_in_deg_per_sec = speed_in_cm_per_sec / (2 * 3.14 * 2.8) * 360
#     degrees_to_turn = 50 / (2 * 3.14 * 2.8) * 360

#     left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)
#     right_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=speed_in_deg_per_sec)

#     while left_motor.is_running or right_motor.is_running:
#         current_angle = gyro_sensor.angle
#         error = current_angle - target_angle
#         correction_factor = error / 10
#         left_motor.speed_sp = speed_in_deg_per_sec + correction_factor
#         right_motor.speed_sp = speed_in_deg_per_sec - correction_factor

#         if ultrasonic_sensor.distance_inches <= 1.3:
#                     left_motor.off(brake=True); right_motor.off(brake=True)
#                     break
    
#     actual_distance = (left_motor.position + right_motor.position) / 2 / 360 * (2 * 3.14 * 2.8)

#     print('Actual approach distance:', actual_distance)
    

#     left_motor.reset(); right_motor.reset(); gyro_sensor.reset()
#     wait(2)

#     liftdrop_object(sign=1)
    