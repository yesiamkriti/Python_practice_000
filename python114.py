# *args with normal parameter
def multiply_num(num8,num9,*arg):
    mul = 1
    for i in arg:
        mul*=i
    return mul
print(multiply_num(2,5,87,54,25,6,55,45))
#  *arg is used for packing
def multiply_num(*args):
    mul = 1
    for i in num2:
        mul*=i
    return mul
num2=[1,2,3,4,5,7]
print(multiply_num(*num2)) # unpack