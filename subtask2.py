#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54

def main1():
    turn(180)
    drive(inches_to_cm(6), OBJECT_ON_OFF= True)
    turn(-90)
    drive(inches_to_cm(96), OBJECT_ON_OFF= True)
    turn(-90)
    drive(inches_to_cm(6), OBJECT_ON_OFF= True)

def main2():
    turn(180)
    drive(inches_to_cm(-6), OBJECT_ON_OFF= True)
    turn(-90)
    drive(inches_to_cm(-36), OBJECT_ON_OFF= True)
    turn(-90)
    drive(inches_to_cm(-6), OBJECT_ON_OFF= True)

if __name__ == '__main__':
    main2()



