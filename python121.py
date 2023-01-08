# iterator vs iterables
numbers =[1,2,3,4] # iterables
squares = map(lambda a: a**2,numbers)#iterator
# for i in numbers:
#     print(i)
print(next(iter(numbers)))
print(next(squares))
# number is iterable so we have to convert it in iterator first then it became iterator 
# if fun is iterator then just apply next funtion it will print the reqired answer
