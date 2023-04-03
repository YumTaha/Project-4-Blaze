from time import sleep as wait

def sleep_between_lines(func):
    def wrapper(*args, **kwargs):
        lines = func(*args, **kwargs)
        if len(lines) == 1: lines()
        else: 
            for line in lines: 
                line(); wait(1)
    return wrapper

