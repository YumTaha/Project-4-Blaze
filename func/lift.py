from ev3dev2.motor import MediumMotor

LIFT_MOTOR_PORT = 'outB'
LIFT_MOTOR_POWER = -10
LIFT_MOTOR_DEGREE = 90

lift_motor = MediumMotor(LIFT_MOTOR_PORT)

def lift_object():
    lift_motor.on_for_degrees(LIFT_MOTOR_POWER, LIFT_MOTOR_DEGREE)
