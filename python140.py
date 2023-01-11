from functools import wraps
import time
# cacluate_time
# def func():
# print('this is a function')
# func()
# this function took 3 sec to run
def calculate_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'executing....{function.__name__}')
        t1 = time.time()
        returned_value = function(*args,**kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f'this function took {total_time}seconds')
        return returned_value
    return wrapper
@calculate_time 
def square_finder(n):
    return [i**2 for i in range(1,n+1)]
print(square_finder(100))
