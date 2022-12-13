# common elements finder function
# define a functions which take 2 lists as input and return a list which contain common elements of both lists
# example
# input -----> [1,2,5,8],[1,2,7,6]
# output -----> [1,2]
def fun(list1,list2):
    list3=[]
    for x in list1:
        if x in list2:
                list3.append(x)
    return list3
print(fun([1,2,5,8],[1,2,7,6]))