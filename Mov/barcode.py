from ev3dev2.motor import MediumMotor, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
from Mov.drive import slowly_approach
from time import sleep as wait

BOXTYPE = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}


# def read_barcode():

#     medium_motor = MediumMotor(OUTPUT_B)
#     color_sensor = ColorSensor()

#     medium_motor.duty_cycle_sp = 100
#     medium_motor.speed_sp = -23

#     medium_motor.run_forever()

#     barcode = []
#     wait(2)
#     while len(barcode) < 4:
#         wait(1.35)

#         color = color_sensor.color

#         if color == ColorSensor.COLOR_BLACK:
#             # Append 1 to the barcode list for black
#             # print("black")
#             barcode.append(1)
#         elif color == ColorSensor.COLOR_WHITE:
#             # Append 0 to the barcode list for white
#             # print("white")
#             barcode.append(0)

#     medium_motor.stop()

#     return barcode

# AROUND 5 AND 6 INCHES BETWEEN CENTER OF THE WHEEL TO THE BARCODE (5.5)

# this function returns bool
def lift_and_scan(type_of_box):
    boxType = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}
    
    barcode = []

    lift_motor = MediumMotor(OUTPUT_B)
    lift_motor.speed_sp = -25
    lift_motor.stop_action = 'hold'
    lift_motor.position_sp = -90

    color_sensor = ColorSensor()

    while True:
        lift_motor.run_to_abs_pos()

        wait(2.5)
        while len(barcode) < 4:
            color = color_sensor.color
            if color == ColorSensor.COLOR_BLACK:
                # Append 1 to the barcode list for black
                print("black")
                barcode.append(1)
            elif color == ColorSensor.COLOR_WHITE:
                # Append 0 to the barcode list for white
                print("white")
                barcode.append(0)
            wait(.8)

        for box_name in boxType:
            if boxType[box_name] == barcode:
                if barcode == type_of_box:
                    slowly_approach()
                    # return True
                return False

        print('Invalid barcode, scanning downward...')

        lift_motor.position_sp = 90
        lift_motor.run_to_abs_pos()
        barcode.reverse()
        while len(barcode) < 4:
            lift_motor.speed_sp = 15
            color = color_sensor.color
            if color == ColorSensor.COLOR_BLACK:
                # Append 1 to the barcode list for black
                print("black")
                barcode.append(1)
            elif color == ColorSensor.COLOR_WHITE:
                # Append 0 to the barcode list for white
                print("white")
                barcode.append(0)
            wait(.5)

        for box_name in boxType:
            if boxType[box_name] == barcode:
                if barcode == type_of_box:
                    slowly_approach()
                    # return True
                return False

        print('Invalid barcode, scanning upward...')
        barcode = []

def scan_barcode(type_of_box):
    box_type = []

    col_sensor = ColorSensor()
    motor = MediumMotor()

    motor.on_for_degrees(10, 10)
    motor.off()
    wait(1)
    motor.position = 0

    motor.on_for_degrees(-10, 56.32)

    while True:
        # print(col_sensor.color)
        if col_sensor.color == 1: box_type.append(1)
        if col_sensor.color == 6: box_type.append(0)
        print(box_type)


        wait(2)
        for i in range(3):
            wait(1)
            motor.on_for_degrees(-10, 13.28)  # move the motor upward by 0.5 inches
            wait(1)
            if col_sensor.color == 1: box_type.append(1)
            if col_sensor.color == 6: box_type.append(0)
            print(box_type)
            wait(1)

        motor.off()
        print('final ', box_type)

        # Check if the scanned barcode matches any of the predefined barcode combinations
        if box_type == BOXTYPE['BoxType 1'] or box_type == BOXTYPE['BoxType 2'] or box_type == BOXTYPE['BoxType 3'] or box_type == BOXTYPE['BoxType 4']:
            if box_type == type_of_box: return True
            else: return False

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
            motor.on_for_degrees(10, 13.05)  # move the motor downward by 0.5 inches
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
            if box_type == type_of_box: return True
            else: return False
        