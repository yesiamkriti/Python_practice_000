# decorators - enhance the funcyionallity of other functions
def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        any_function()
    return wrapper_function
def fun1():
    print("this is function 1")
def fun2():
    print("this is function 2")
var = decorator_function(fun1)
func2 = decorator_function(fun2)
var()
func2()
# shortcut of decorator function
# for decorator function we use @ 
@decorator_function
def func3():
    print("@ is use for decorator function")
func3()