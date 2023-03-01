#!/usr/bin/env python3

from Movement.reader import read_barcode, read_black, box
from time import sleep
from ev3dev2.sound import Sound
from Movement.drive import turn_degree, drive_straight
from ev3dev2.console import Console

'''THIS IS WHERE I CHECK THE VURNABILITY OF EACH FUNCTION AND HOW WELL THEY WORK'''


def main():
    inch = 36
    cm = inch * 2.54
    drive_straight(cm, 20)


if __name__ == '__main__':
    main()
