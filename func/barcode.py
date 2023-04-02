from ev3dev2.motor import MediumMotor, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
from func.drive import slowly_approach
from time import sleep as wait

# BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}
BOXTYPE = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [1, 0, 1, 0], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}

UPWARD_ANGLE = 13.4
DOWNWARD_ANGLE = 13.1

# AROUND 5 AND 6 INCHES BETWEEN CENTER OF THE WHEEL TO THE BARCODE (5.5)
# ULTRASONIC AROUND 2.5 INCHES
def scan_barcode(type_of_box):

    col_sensor = ColorSensor()
    motor = MediumMotor()

    motor.on_for_degrees(10, 7)
    motor.off()
    wait(.5)
    motor.position = 0

    motor.on_for_degrees(-10, 56.55)

    for var in range(4):
        if var == 3: DOWNWARD_ANGLE = UPWARD_ANGLE

        box_type = []
        if col_sensor.color == 1: box_type.append(1)
        if col_sensor.color == 6: box_type.append(0)
        print(box_type)


        wait(2)
        for i in range(3):
            wait(1)
            motor.on_for_degrees(-10, UPWARD_ANGLE)  # move the motor upward by 0.5 inches
            wait(1)
            if col_sensor.color == 1: box_type.append(1)
            if col_sensor.color == 6: box_type.append(0)
            print(box_type)
            wait(1)

        motor.off()
        print('final ', box_type)

        # Check if the scanned barcode matches any of the predefined barcode combinations
        if box_type == BOXTYPE['BoxType 1'] or box_type == BOXTYPE['BoxType 2'] or box_type == BOXTYPE['BoxType 3'] or box_type == BOXTYPE['BoxType 4']:
            wait(2)
            motor.on_for_degrees(10, 13.05 * 3 + 55) # Coming down to the right level to pickup the box
            wait(.5)
            if box_type == type_of_box: 
                print('Lifting the box...')
                wait(1)
                slowly_approach()
                OBJECT_ON_OFF = False
                return OBJECT_ON_OFF
            else: return True

        wait(3)
        print('scanning downward...')
        box_type = []

        # Repeat the scanning process in the opposite direction
        if col_sensor.color == 1: box_type.append(1)
        if col_sensor.color == 6: box_type.append(0)
        print(box_type)
        wait(1)
        for i in range(3):
            wait(1)
            motor.on_for_degrees(10, DOWNWARD_ANGLE)  # move the motor downward by 0.5 inches
            wait(1)

            if col_sensor.color == 1: box_type.append(1)
            if col_sensor.color == 6: box_type.append(0)
            print(box_type)
            wait(1)

        motor.off()

        box_type.reverse()
        print('reversed ', box_type)
        # Check if the scanned barcode matches any of the predefined barcode combinations
        if box_type == BOXTYPE['BoxType 1'] or box_type == BOXTYPE['BoxType 2'] or box_type == BOXTYPE['BoxType 3'] or box_type == BOXTYPE['BoxType 4']:
            wait(.5)
            if box_type == type_of_box: 
                print('Lifting the box...')
                wait(1)
                slowly_approach()
                OBJECT_ON_OFF = False
                return OBJECT_ON_OFF
            else: return True
        