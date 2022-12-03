numbers =[1,2,3,4,5,2,6]
#write a program to turn item of list into its square
#output - [1,4,9,16,25]
newlist=[x*x for x in numbers]
print(newlist)
# in the above list, find value 2, if it is present,
# replace it with 200, only update the first occurance
b=numbers.index(2)
numbers[b]=200
print(numbers)
num2=numbers.copy()
print(numbers)
numb3=list(numbers)
print(numbers)
list1 = ["x","y","z"]
list2 = [1,2,3,4]
list3 = list1 + list2
print(list3)
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
print(list1)
for i in list2:
    list1.append(i)
print(list1)
#insert()-insert item at specified index
#append()-insert item at the end of the list
#extend()-it appends elements from one list to another list, it can be used to append different collection
#remove()-remvoes item from a specified index
#pop()-removes the element at the specified position.
#clear()-clears all element
#len()-find length of a list
#sort()-arrange elements of list(default ascending)
#reverse()-arrange in descending
#copy()-copy a variable in a list