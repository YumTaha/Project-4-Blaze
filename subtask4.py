#!/usr/bin/env python3
from INFO import *
from func.drive import *
from func.turn import *
from func.barcode import *
from func.lift import *
from func.sound import *

def main():
    liftdrop_object(sign=1)
    drive(inches_to_cm(42 - LOCATION_X[BOX_NUMBER]), OBJECT_ON_OFF= False)
    liftdrop_object(sign=-1)

if __name__ == '__main__':
    main()



