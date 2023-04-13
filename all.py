#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    drive(inches_to_cm(37.2 + SHELVE), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(0.5), OBJECT_ON_OFF= True)

    OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE[TYPE])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO')
    else: print('This barcode is the right one? YES')

    if LOCATION_HOME == 'A':
        turn(180)
        drive(inches_to_cm(.5 + LOCATION_X[BOX_NUMBER]), OBJECT_ON_OFF)
        turn(-90)
        drive(inches_to_cm(37.2 + SHELVE), OBJECT_ON_OFF)

    elif LOCATION_HOME == 'B':
        drive(inches_to_cm(94 - (LOCATION_X[BOX_NUMBER] - ROW)), OBJECT_ON_OFF)
        turn(90)
        drive(inches_to_cm(37.2 + SHELVE), OBJECT_ON_OFF)

    elif LOCATION_HOME == 'C':
        turn(180)
        drive(inches_to_cm(37.2 + SHELVE), OBJECT_ON_OFF)
        turn(90)
        drive(inches_to_cm(D - (37.2 + SHELVE)), OBJECT_ON_OFF)

    elif LOCATION_HOME == 'D':
        drive(inches_to_cm(94 - (LOCATION_X[BOX_NUMBER] - ROW)), OBJECT_ON_OFF)
        turn(-90)
        drive(inches_to_cm(D - (37.2 + SHELVE)), OBJECT_ON_OFF)

    if OBJECT_ON_OFF: pass
    else: liftdrop_object(sign=-1)

if __name__ == '__main__':
    main()



