from ev3dev2.motor import MediumMotor
from ev3dev2.sensor.lego import ColorSensor
from func.drive import *
from func.sound import *
from time import sleep as wait

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

UPWARD_ANGLE = 13.43
DOWNWARD_ANGLE = 13.05

# AROUND 5 AND 6 INCHES BETWEEN CENTER OF THE WHEEL TO THE BARCODE (5.5)
# ULTRASONIC AROUND 2.5 INCHES
def scan_barcode(type_of_box):
    col_sensor = ColorSensor(); motor = MediumMotor()


    for var in range(4):
        wait(1)
        print('Scanning upward...')
        box_type = []
        if col_sensor.color == 1: box_type.append(1)
        if col_sensor.color == 6: box_type.append(0)
        print(box_type); play_sound(col_sensor.color_name)

        wait(1)
        for i in range(3):
            motor.on_for_degrees(-10, UPWARD_ANGLE)  # move the motor upward by 0.5 inches
            wait(1)
            if col_sensor.color == 1: box_type.append(1)
            if col_sensor.color == 6: box_type.append(0)
            print(box_type); play_sound(col_sensor.color_name)
            wait(1)

        motor.off()
        print('final ', box_type)
        if len(box_type) <=3: 
            print('Incorrect scanning...'); motor.on_for_degrees(-10, UPWARD_ANGLE)
            wait(.5)

        # Check if the scanned barcode matches any of the predefined barcode combinations
        if box_type in BOXTYPE.values():
            wait(1)
            motor.on_for_degrees(10, UPWARD_ANGLE * 3 + 56) # Coming down to the right level to pickup the box
            if box_type == type_of_box: 
                play_sound('Lifting the box...'); wait(1); slowly_approach()
                OBJECT_ON_OFF = False
                return OBJECT_ON_OFF
            else: return True

        wait(2)
        print('Scanning downward...')
        box_type = []

        # Repeat the scanning process in the opposite direction
        if col_sensor.color == 1: box_type.append(1)
        if col_sensor.color == 6: box_type.append(0)
        print(box_type); play_sound(col_sensor.color_name)
        
        wait(1)
        for i in range(3):
            motor.on_for_degrees(10, DOWNWARD_ANGLE)  # move the motor downward by 0.5 inches
            wait(1)
            if col_sensor.color == 1: box_type.append(1)
            if col_sensor.color == 6: box_type.append(0)
            print(box_type); play_sound(col_sensor.color_name)
            wait(1)

        motor.off(); box_type.reverse()
        print('reversed ', box_type)
        if len(box_type) <=3: 
            print('Incorrect scanning...'); motor.on_for_degrees(-10, UPWARD_ANGLE)
            wait(.5)

        # Check if the scanned barcode matches any of the predefined barcode combinations
        if box_type in BOXTYPE.values():
            motor.on_for_degrees(10, 56.6) # Coming down to the right level to pickup the box
            if box_type == type_of_box: 
                play_sound('Lifting the box...'); wait(1); slowly_approach()
                OBJECT_ON_OFF = False
                return OBJECT_ON_OFF
            else: return True
        