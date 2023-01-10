from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''this is a wrap function'''
        print('this is awesome function')
        return any_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def add(a,b):
    '''this is  add function'''
    return a+b
print(add.__doc__) # this is docstring
print(add.__name__)
print(add(25,36))
# here we are not getting add as answer because add.__name__ is calling wrapper_function.....to call add function we have to import a module "from functools import wrap" after this we ahve to write @wraps (any_function)