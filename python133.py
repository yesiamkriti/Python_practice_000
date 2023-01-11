# funtion as an argument 
# map
def square(a):
    return a**2

l = [1,2,3,4,5,6,7,8,9]
print(list(map(square,l)))

def my_map(func,l):
    new_list = []
    for item in l :
        new_list.append(func(item))
    return new_list
def my_map2(func,l):
    return[func(item) for item in l]
print(my_map(lambda a : a**3,l))
print(my_map2(lambda a : a**5,l))