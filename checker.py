#!/usr/bin/env python3

from Movement.color_reader import read_barcode
from Movement.drive import drive_straight

def main():
    #barcode = read_barcode()
    #print(barcode)
    drive_straight(40, 20)


if __name__ == '__main__':
    main()
