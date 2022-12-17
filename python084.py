# function return two values
def func(int1, int2):
    add = int1 +int2
    multiply = int1 * int2
    return add , multiply
print(func(2,3))# here we get answer in tuple form if we write add,multiple two diff values
# if we want to print normal we have to write like this
add,multiply = func(2,3)
print(add)
print(multiply)