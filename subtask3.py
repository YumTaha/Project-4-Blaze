#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54
# 0 = WHITE
# 1 = BLACK

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

def main():
    # drive(inches_to_cm(0.5), OBJECT_ON_OFF= True)
    # OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE['BoxType 2'])
    # if OBJECT_ON_OFF: print('This barcode is the right one? NO'); play_sound('MALEEK')
    # else: print('This barcode is the right one? YES'); play_sound('MALEEK'); beep()
    drive(40, OBJECT_ON_OFF=True)
    turn(90)
    drive(20, OBJECT_ON_OFF=True)    
    turn(90)
    drive(40, OBJECT_ON_OFF=True)    
    turn(90)
    drive(20, OBJECT_ON_OFF=True)    
    turn(90)
    drive(inches_to_cm(0.5), OBJECT_ON_OFF= True)
    OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE['BoxType 2'])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO'); play_sound('MALEEK')
    else: print('This barcode is the right one? YES'); play_sound('MALEEK'); beep()
    drive(inches_to_cm(4), OBJECT_ON_OFF= True)
    liftdrop_object(-1)
    turn(-10)
    drive(inches_to_cm(-10), OBJECT_ON_OFF= True)
    turn(500)


    


if __name__ == '__main__':
    main()



