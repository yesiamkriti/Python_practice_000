""" filter odd even
define a function
input
list -----> [1,2,3,4,5,6,7]

output ------> [[1,3,5,7],[2,4,6]]"""
def function(list1):
    list2=[]
    list3=[]
    for x in list1:
        if x%2 == 0 :
            list2.append(x)
        else:
            list3.append(x)
    return [list2,list3]
list1=[1,2,3,4,5,6,7]
print(function(list1))

