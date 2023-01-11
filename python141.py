from functools import wraps
def only_integers(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_type = []
        if all([type(i)==int for i in args]):
            return function(*args,**kwargs)
        print("Invalid")
    return wrapper
@only_integers
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5,6,7,89,[4,9,0]))