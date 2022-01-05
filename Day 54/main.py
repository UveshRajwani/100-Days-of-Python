# import time
#
# current_time = time.time()
#
#
# def speed_calc_decorator(fun):
#     current_time = time.time()
#     fun_time= fun()
#     print(current_time-fun_time)
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
#     current_time = time.time()
#     return current_time
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#     current_time = time.time()
#     return current_time
#
# fast_function
# slow_function

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
