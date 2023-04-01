# def ErrorHandler(func):
#     def wrapper(*args):
#         try:
#             func(*args)
#         except TypeError:
#             print("TypeError")
#         except ZeroDivisionError:
#             print("ZeroDivisionError")
#         except ValueError:
#             print("ValueError")
#         except Exception as e:
#             print(e)
#     return wrapper

# @ErrorHandler
# def test():
#     return 1/0

# @ErrorHandler
# def test2(n):
#     if n == 0:
#         raise ZeroDivisionError
#     print(n)

def remove_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            if isinstance(result, (tuple, list)):
                return [item for item in result if item is not None]
            else:
                return result
    return wrapper



