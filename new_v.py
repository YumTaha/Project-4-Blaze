#!/usr/bin/env python3

from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

play_sound('fire_force.mp3')
play_sound('time_stop.mp3')


# BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}
BOXTYPE = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [1, 0, 1, 0], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}


def main():
    # turn(360)
    # barcode = read_barcode()
    # print(barcode)
    # lift_and_scan(BOXTYPE['BoxType 1'])
    # lift_object()
    # drive_forward(60, OBJECT_ON_OFF= True)
    # OBJECT_ON_OFF = scan_barcode(BOXTYPE['BoxType 2'])
    # drive_forward(30, OBJECT_ON_OFF)

    # if OBJECT_ON_OFF: print('This barcode is the right one? NO')
    # else: print('This barcode is the right one? YES')
    pass
    


if __name__ == '__main__':
    main()



