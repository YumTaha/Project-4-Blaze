from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
import ev3dev2.sensor.lego as sensor

GYRO_PORT = 'in1'
SPEED = 20
gyro = sensor.GyroSensor(GYRO_PORT)
GYRO_INITIAL = gyro.angle


def turn(degrees, direction='right'):
    gyro.reset()
    
    speed_turn = int(SPEED / 4)

    left_motor, right_motor = LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_D)
    left_motor.reset()
    right_motor.reset()

    if degrees > 0:
        if direction == 'right':
            left_speed = speed_turn
            right_speed = -speed_turn
        elif direction == 'left':
            left_speed = -speed_turn
            right_speed = speed_turn

    while True:
        angle = gyro.angle - GYRO_INITIAL

        if abs(angle - degrees) > 1:
            if angle > degrees:
                left_speed = -speed_turn if direction == 'right' else speed_turn
                right_speed = speed_turn if direction == 'right' else -speed_turn
            else:
                left_speed = speed_turn if direction == 'right' else -speed_turn
                right_speed = -speed_turn if direction == 'right' else speed_turn

            left_motor.on(speed=left_speed)
            right_motor.on(speed=right_speed)
        else:
            gyro.reset()
            left_motor.off(brake=True)
            right_motor.off(brake=True)
            break
        
    print("Actual angle turned:", angle)