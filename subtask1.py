#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54

BOX_WIDTH = 6
STOP_WHERE = BOX_WIDTH//2
LOCATION = {'7': STOP_WHERE, '8': STOP_WHERE+6, '9': STOP_WHERE+12, '10': STOP_WHERE+18, '11': STOP_WHERE+24, '12': STOP_WHERE+30}
BOX_NUMBER = '9'

def main():
    drive(inches_to_cm(36), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(6 + LOCATION[BOX_NUMBER]), OBJECT_ON_OFF= True)
    wait(5)
    drive(inches_to_cm(90 - LOCATION[BOX_NUMBER]), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(36), OBJECT_ON_OFF= True)

if __name__ == '__main__':
    main()



