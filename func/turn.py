from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.sensor.lego import GyroSensor as GS

SPEED = 20
gyro = GS('in1')
GYRO_INITIAL = gyro.angle


def turn(degrees, dirc='right'):
    gyro.reset()
    
    speed_turn = int(SPEED / 4)

    left_motor, right_motor = LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_D)
    left_motor.reset(); right_motor.reset()

    if degrees > 0:
        if dirc == 'right':
            left_speed = speed_turn; right_speed = -speed_turn
        elif dirc == 'left':
            left_speed = -speed_turn; right_speed = speed_turn

    while True:
        angle = gyro.angle - GYRO_INITIAL

        if abs(angle - degrees) > 1:
            left_speed = -speed_turn if dirc == 'right' else speed_turn
            right_speed = speed_turn if dirc == 'right' else -speed_turn

            if angle <= degrees:
                left_speed, right_speed = right_speed, left_speed


            left_motor.on(speed=left_speed); right_motor.on(speed=right_speed)
        else:
            gyro.reset()
            left_motor.off(brake=True); right_motor.off(brake=True)
            break
        
    print("Actual angle turned:", angle)