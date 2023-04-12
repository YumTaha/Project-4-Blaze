#!/usr/bin/env python3
from func.drive import *
from INFO import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54
# 0 = WHITE
# 1 = BLACK

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}
STOP_WHERE = 3
LOCATION = {'7': STOP_WHERE, '8': STOP_WHERE+6, '9': STOP_WHERE+12, '10': STOP_WHERE+18, '11': STOP_WHERE+24, '12': STOP_WHERE+30}


def main():
    # drive(inches_to_cm(1), OBJECT_ON_OFF= True)
    OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE[TYPE])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO')
    else: print('This barcode is the right one? YES')
    drive(inches_to_cm(37 - LOCATION[BOX_NUMBER]), OBJECT_ON_OFF= False)
    liftdrop_object(sign=-1)
    
    


if __name__ == '__main__':
    main()



