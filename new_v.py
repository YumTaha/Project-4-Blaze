#!/usr/bin/env python3
from func.decorators import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def inches_to_cm(inches): return inches * 2.54

BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0], 'special': [1, 0, 1, 0]}

@sleep_between_lines
def main():
    drive_forward(inches_to_cm(18), OBJECT_ON_OFF= True, start='yes')
    turn(90)
    drive_forward(inches_to_cm(18), OBJECT_ON_OFF= True)
    OBJECT_ON_OFF = scan_barcode(BOXTYPE['special'])
    drive_forward(inches_to_cm(18), OBJECT_ON_OFF)
    if OBJECT_ON_OFF: print('This barcode is the right one? NO'); play_sound('wrong barcode')
    else: print('This barcode is the right one? YES'); play_sound('correct barcode'); beep()
    # pass
    


if __name__ == '__main__':
    main()



