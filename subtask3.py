#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    drive(inches_to_cm(1), OBJECT_ON_OFF= True)
    OBJECT_ON_OFF = scan_barcode_hor_reflect(BOXTYPE[TYPE])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO')
    else: print('This barcode is the right one? YES')

if __name__ == '__main__':
    main()



