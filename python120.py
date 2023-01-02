# filter function
def is_even(a):
    return a%2 == 0
numbers = [1,2,3,4,5,6,7,8,9,10]
print(tuple(filter(is_even,numbers)))
# or
print(tuple(filter(lambda b : b%2==0,range(1,11))))
# iterate means to print one by one each successful condition
# example of iterate

print(i for i in range(1,11) if i%2==0)
# map and filter can iterate only once 

