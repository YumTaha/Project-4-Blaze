from ev3dev2.motor import MediumMotor, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from func.drive import *
from func.turn import *
from func.sound import *
from time import sleep as wait

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

UPWARD_ANGLE = 13.4
DOWNWARD_ANGLE = 13
DIS_SECOND = 0.245
BACK_ROTATIONS = 0.5
ROTATIONS = 0.37

# AROUND 5 AND 6 INCHES BETWEEN CENTER OF THE WHEEL TO THE BARCODE (5.5)
# ULTRASONIC AROUND 2.5 INCHES
# def scan_barcode(type_of_box):
#     col_sensor = ColorSensor('in2'); motor = MediumMotor()


#     for var in range(4):
#         wait(1)

#         print('Scanning upward...')
#         box_type = []
#         if col_sensor.reflected_light_intensity < 30: box_type.append(1); play_sound('black')
#         else: box_type.append(0); play_sound('white')
#         print(box_type)

#         wait(1)
#         for i in range(3):
#             motor.on_for_degrees(-10, UPWARD_ANGLE)  # move the motor upward by 0.5 inches
#             wait(1)
#             if col_sensor.reflected_light_intensity < 30: box_type.append(1); play_sound('black')
#             else: box_type.append(0); play_sound('white')
#             print(box_type)

#         motor.off()
#         print('final ', box_type)
#         if len(box_type) !=4: 
#             print('Incorrect scanning...'); motor.on_for_degrees(-10, UPWARD_ANGLE)
#             wait(.5)
#         else:
#             # Check if the scanned barcode matches any of the predefined barcode combinations
#             if box_type in BOXTYPE.values():
#                 wait(1)
#                 motor.on_for_degrees(10, UPWARD_ANGLE * 3 + 56) # Coming down to the right level to pickup the box
#                 if box_type == type_of_box: 
#                     play_sound('Lifting the box...'); wait(1); slowly_approach()
#                     OBJECT_ON_OFF = False
#                     return OBJECT_ON_OFF
#                 else: return True

#         wait(2)
#         print('Scanning downward...')
#         box_type = []

#         # Repeat the scanning process in the opposite direction
#         if col_sensor.reflected_light_intensity < 30: box_type.append(1); play_sound('black')
#         else: box_type.append(0); play_sound('white')
#         print(box_type)
        
#         wait(1)
#         for i in range(3):
#             motor.on_for_degrees(10, DOWNWARD_ANGLE)  # move the motor downward by 0.5 inches
#             wait(1)
#             if col_sensor.reflected_light_intensity < 30: box_type.append(1); play_sound('black')
#             else: box_type.append(0); play_sound('white')
#             print(box_type)
#             wait(1)

#         motor.off(); box_type.reverse()
#         print('reversed ', box_type)
#         if len(box_type) <=3: 
#             print('Incorrect scanning...'); motor.on_for_degrees(-10, UPWARD_ANGLE)
#             wait(.5)

#         # Check if the scanned barcode matches any of the predefined barcode combinations
#         if box_type in BOXTYPE.values():
#             motor.on_for_degrees(10, 56.6) # Coming down to the right level to pickup the box
#             if box_type == type_of_box: 
#                 play_sound('Lifting the box...'); wait(1); slowly_approach()
#                 OBJECT_ON_OFF = False
#                 return OBJECT_ON_OFF
#             else: return True

def scan_barcode_hor_colors(type_of_box):
    col_sensor = ColorSensor('in4')
    tank_drive = MoveTank('outA', 'outD')
    
    while col_sensor.color not in [4, 7]: tank_drive.on(10, 10); print(col_sensor.color_name)
    tank_drive.off()
    print(col_sensor.color_name)

    tank_drive.on_for_rotations(10,10,ROTATIONS)
    tank_drive.off()

    for i in range(4):
        wait(1)

        

        print('Scanning barcode...')
        box_type = []
        if col_sensor.color not in [1, 2]: box_type.append(1)
        if col_sensor.color not in [4, 6]: box_type.append(0)
        print(box_type); play_sound(col_sensor.color_name)

        # Repeat the scanning process for 3 more colors
        for j in range(3):
            wait(1)
            tank_drive.on_for_seconds(10, 10, DIS_SECOND)
            tank_drive.off()

            if col_sensor.color not in [1, 2]: box_type.append(1)
            if col_sensor.color not in [4, 6]: box_type.append(0)
            print(box_type); play_sound(col_sensor.color_name)

        print('final ', box_type)
        if len(box_type) != 4:
            print('Incorrect scanning...'); wait(1)
        else:
            # Check if the scanned barcode matches any of the predefined barcode combinations
            if box_type in BOXTYPE.values():
                wait(1)
                if box_type == type_of_box:
                    play_sound('Lifting the box...')
                    tank_drive.on_for_rotations(-10,-10,BACK_ROTATIONS)
                    wait(0.5)
                    turn(60) #Turning
                    wait(0.5)
                    tank_drive.on_for_seconds(-10,-10,0.4)
                    wait(0.5)
                    turn(30)
                    wait(0.5)
                    tank_drive.on_for_seconds(10,10,1)
                    wait(0.5)
                    liftdrop_object(sign=1)
                    OBJECT_ON_OFF = False
                    return OBJECT_ON_OFF
                else: return True

        wait(2)
        print('Scanning backward...')
        box_type = []

        # Repeat the scanning process in the opposite direction
        if col_sensor.color not in [1, 2]: box_type.append(1)
        if col_sensor.color not in [4, 6]: box_type.append(0)
        print(box_type); play_sound(col_sensor.color_name)
        
        wait(1)
        for i in range(3):
            wait(1)
            tank_drive.on_for_seconds(-10, -10, DIS_SECOND)
            tank_drive.off()

            if col_sensor.color not in [1, 2]: box_type.append(1) #Black or Blue
            if col_sensor.color not in [4, 6]: box_type.append(0) #White or Yellow
            print(box_type); play_sound(col_sensor.color_name)
            wait(1)

        box_type.reverse()
        print('reversed ', box_type)
        if len(box_type) !=4: 
            print('Incorrect scanning...')
            wait(.5)
        else:
            # Check if the scanned barcode matches any of the predefined barcode combinations
            if box_type in BOXTYPE.values():
                wait(1)
                if box_type == type_of_box:
                    play_sound('Lifting the box...')
                    tank_drive.on_for_rotations(-10,-10,0.1)
                    wait(0.5)
                    turn(70) #Turning
                    wait(0.5)
                    tank_drive.on_for_seconds(-10,-10,0.4)
                    wait(0.5)
                    turn(20)
                    wait(0.5)
                    tank_drive.on_for_seconds(10,10,1)
                    wait(0.5)
                    liftdrop_object(sign=1)
                    OBJECT_ON_OFF = False
                    return OBJECT_ON_OFF
                else: return True 

        print('scanning forward...')

def scan_barcode_hor_reflect(type_of_box):
    col_sensor = ColorSensor('in4')
    tank_drive = MoveTank('outA', 'outD')
    
    while col_sensor.color not in [4, 7]: tank_drive.on(10, 10); print(col_sensor.color_name)
    tank_drive.off()
    print(col_sensor.color_name)

    tank_drive.on_for_rotations(10,10,ROTATIONS)
    tank_drive.off()
    col_sensor.mode = 'COL-REFLECT'
    for i in range(4):
        wait(1)
        
        

        print('Scanning barcode...')
        box_type = []
        if col_sensor.reflected_light_intensity < 30: box_type.append(1) #black
        else: box_type.append(0) #White
        print(box_type)

        # Repeat the scanning process for 3 more colors
        for j in range(3):
            wait(1)
            tank_drive.on_for_seconds(10, 10, DIS_SECOND)
            tank_drive.off()

            if col_sensor.reflected_light_intensity < 30: box_type.append(1) #black
            else: box_type.append(0) #White
            print(box_type)

        print('final ', box_type)
        if len(box_type) != 4:
            print('Incorrect scanning...'); wait(1)
        else:
            # Check if the scanned barcode matches any of the predefined barcode combinations
            if box_type in BOXTYPE.values():
                wait(1)
                if box_type == type_of_box:
                    play_sound('Lifting the box...')
                    tank_drive.on_for_rotations(-10,-10,BACK_ROTATIONS)
                    wait(0.5)
                    turn(60) #Turning
                    wait(0.5)
                    tank_drive.on_for_seconds(-5,-5,1)
                    turn(25)
                    tank_drive.on_for_seconds(10,10,1)
                    liftdrop_object(sign=1)
                    tank_drive.on_for_seconds(-5,-5,1)
                    wait(3)
                    turn(-90)
                    OBJECT_ON_OFF = False
                    return OBJECT_ON_OFF
                else: return True

        wait(2)
        print('Scanning backward...')
        box_type = []

        # Repeat the scanning process in the opposite direction
        if col_sensor.reflected_light_intensity < 30: box_type.append(1) #black
        else: box_type.append(0) #White
        print(box_type)
        
        wait(1)
        for i in range(3):
            wait(1)
            tank_drive.on_for_seconds(-10, -10, DIS_SECOND)
            tank_drive.off()

            if col_sensor.reflected_light_intensity < 30: box_type.append(1) #black
            else: box_type.append(0) #White
            print(box_type)
            wait(1)

        box_type.reverse()
        print('reversed ', box_type)
        if len(box_type) !=4: 
            print('Incorrect scanning...')
            wait(.5)
        else:
            # Check if the scanned barcode matches any of the predefined barcode combinations
            if box_type in BOXTYPE.values():
                wait(1)
                if box_type == type_of_box:
                    play_sound('Lifting the box...')
                    tank_drive.on_for_rotations(-10,-10,0.1)
                    wait(0.5)
                    turn(60) #Turning
                    wait(0.5)
                    tank_drive.on_for_seconds(-5,-5,1)
                    turn(25)
                    tank_drive.on_for_seconds(10,10,1)
                    liftdrop_object(sign=1)
                    tank_drive.on_for_seconds(-5,-5,1)
                    wait(3)
                    turn(-98)
                    OBJECT_ON_OFF = False
                    return OBJECT_ON_OFF
                else: return True 

        print('scanning forward...')
