#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

# chelve length 36 inches
# 
def main():
    liftdrop_object(sign=1)
    drive(inches_to_cm(-3), OBJECT_ON_OFF= True)
    turn(90)
    drive(inches_to_cm(), OBJECT_ON_OFF= True)
    liftdrop_object(sign=-1)
    


if __name__ == '__main__':
    main()



