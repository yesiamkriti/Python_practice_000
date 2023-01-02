# map function
number = [1,2,3,4] # this is an iterable 
def square(a):
    return a**2
# print([square(1),square(2),square(3),square(4)])
# or
print(list(map(square,number)))
# or by using list comprehension
square_new = [i**2 for i in range(1,5)]
print(list(square_new))