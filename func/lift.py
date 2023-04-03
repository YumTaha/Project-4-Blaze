from ev3dev2.motor import MediumMotor
from time import sleep as wait
LIFT_MOTOR_POWER = -10
LIFT_MOTOR_DEGREE = 90

lift_motor = MediumMotor('outB')

def lift_object(): wait(1); lift_motor.on_for_degrees(LIFT_MOTOR_POWER, LIFT_MOTOR_DEGREE)
def drop_object(): wait(1); lift_motor.on_for_degrees(LIFT_MOTOR_POWER, -LIFT_MOTOR_DEGREE)
