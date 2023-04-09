#!/usr/bin/env python3
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *


def inches_to_cm(inches): return inches * 2.54
# 0 = WHITE
# 1 = BLACK

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

def main():
    drive(inches_to_cm(8), OBJECT_ON_OFF= True, start='yes')
    OBJECT_ON_OFF = scan_barcode(BOXTYPE['BoxType 2'])
    if OBJECT_ON_OFF: print('This barcode is the right one? NO'); play_sound('I love doctor KWUIMI')
    else: print('This barcode is the right one? YES'); play_sound('I love doctor KWUIMI'); beep()
    # pass
    


if __name__ == '__main__':
    main()



