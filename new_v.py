#!/usr/bin/env python3

from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *

BOXTYPE = {'BoxType 1': [0, 1, 1, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}


def main():
    drive_forward(30)
    # turn(360)
    # barcode = read_barcode()
    # print(barcode)
    # lift_and_scan(BOXTYPE['BoxType 1'])
    # lift_object()
    # barcode = scan_barcode(BOXTYPE['BoxType 2'])

    # print('This barcode is the right one? ', barcode)
    pass
    


if __name__ == '__main__':
    main()



