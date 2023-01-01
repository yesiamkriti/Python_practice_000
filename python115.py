# def function input
# num,iterable(tuple,list)containing numbers as args 
# example

# nums = [1,2,3]
# to_power(3,*nums)
# output
# list -----> [1,8,27]
# if user did't pass any args then give a user a message 'hey you didn't pass arg'
# else .
# return list 
# note use list comprehension
def power(*args):
    mul=1
    for i in num :
        mul*=i
    return mul
num = [1,2,3]
[1,8,27]