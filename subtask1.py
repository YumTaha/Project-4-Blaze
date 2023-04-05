#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54

def main():
    drive(inches_to_cm(18), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(8), OBJECT_ON_OFF= True)
    wait(2)
    drive(inches_to_cm(88), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(18), OBJECT_ON_OFF= True)

if __name__ == '__main__':
    main()



