#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    turn(180)
    drive(inches_to_cm(12), OBJECT_ON_OFF= True)
    turn(-93)
    drive(inches_to_cm(96), OBJECT_ON_OFF= True)
    turn(-93)
    drive(inches_to_cm(18), OBJECT_ON_OFF= True)

if __name__ == '__main__':
    main()



