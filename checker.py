#!/usr/bin/env python3

from Movement.reader import read_barcode, read_black, box
from time import sleep
from ev3dev2.sound import Sound
from Movement.drive import turn_degree
from ev3dev2.console import Console

'''THIS IS WHERE I CHECK THE VURNABILITY OF EACH FUNCTION AND HOW WELL THEY WORK'''


def main():
    turn_degree(180, 20)
    turn_degree(180, 20)


if __name__ == '__main__':
    main()
