TYPE = 'BoxType 3'
BOX_NUMBER = '9'
ROW = 0 # row2 is 42
LOCATION_HOME = 'C'
SHELVE = 24 * 0 #change the 1 to which shelve
BOXTYPE = {'BoxType 1': [0, 0, 0, 1], 'BoxType 2': [0, 1, 0, 1], 'BoxType 3': [0, 0, 1, 1], 'BoxType 4': [0, 1, 1, 0]}
STOP_WHERE = 3
LOCATION_X = {'7': STOP_WHERE,'8': STOP_WHERE+6, '9': STOP_WHERE+12, '10': STOP_WHERE+18, '11': STOP_WHERE+24, '12': STOP_WHERE+30}
D = 112

def inches_to_cm(inches): return inches * 2.54
