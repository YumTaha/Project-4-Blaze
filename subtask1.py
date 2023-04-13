#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    drive(inches_to_cm(38), OBJECT_ON_OFF= True)
    turn(88)
    drive(inches_to_cm(LOCATION_X[BOX_NUMBER]), OBJECT_ON_OFF= True)
    wait(5)
    drive(inches_to_cm(94 - LOCATION_X[BOX_NUMBER]), OBJECT_ON_OFF= True)
    turn(88)
    drive(inches_to_cm(39), OBJECT_ON_OFF= True)

if __name__ == '__main__':
    main()



