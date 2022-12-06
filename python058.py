from functools import reduce

list1 =[1,2,3,4,5,6,7]
sum = reduce(lambda i,j: i+j,list1)
print(sum)