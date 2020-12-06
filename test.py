import time


def decorator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name + ' must be string')
    return wrapper


@decorator
def f1(param):
    print("with param: " + param)


f1('p1')
