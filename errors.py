def ErrorHandler(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("TypeError")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except ValueError:
            print("ValueError")
        except Exception as e:
            print(e)
    return wrapper

@ErrorHandler
def test():
    return 1/0
test()

@ErrorHandler
def test2(n):
    if n == 0:
        raise ZeroDivisionError
    print(n)
    
test2(0)


