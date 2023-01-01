# make flexible function
# *operator
#  *args
def total(a,b):
    return a+b
print(total(45,7,4,45,34,2,34,545,3,5,35,53,5,5,34,26)) # here we cannot put more than two value so this is showing synatax error
def all_total(*args):
    total = 0
    for num in args:
        total=total+num
    return total
print(all_total(1,2,4,6,7,8,9,6,1,2,25,45,))