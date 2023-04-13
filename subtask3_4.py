#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE[TYPE])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO')
    else: print('This barcode is the right one? YES')
    drive(inches_to_cm(37 - LOCATION_X[BOX_NUMBER]), OBJECT_ON_OFF= False)
    liftdrop_object(sign=-1)
    
if __name__ == '__main__':
    main()



