# list comprehension in nested list
# example = [[1,2,3],[1,2,3],[1,2,3]]
print([[i for i in range(1,4)]for i in range(3)])

# normal
list2 = []
list3 = []
def list1():
    for i in range(1,4):
        b = list3.append(i)
    for j in range(3):
        list2.append(list3)
    return(list2)
print(list1())