# scope
x = 5 #
def func():
    global x # if we write global here then the value of x=7 for 2 also
    x = 7 #local variable
    return x
print(x)
print(func()) #1
print(x) # 2 # here x is not define if we not set global value