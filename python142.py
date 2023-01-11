# decorator with argument
from functools import wraps
def only_datatype(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(i)==data_type for i in args]):
                return function(*args, **kwargs)
            print("Invalid")
        return wrapper
    return decorator
@only_datatype(str)
def str_join(*args):
    string = ""
    for i in args:
        string+=i
    return string
print(str_join('kjkjbkj', 'uguyguyjh'))