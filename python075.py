# list vs array(ordered collection of item)
# array module - fix data type
# javascript array = python list 
# we use numpy arrays for data science
a=(list(range(1,20)))
# poped_item=a.pop()
# print(a)
def negetive_list(l):
    negetive = []
    for i in l:
        negetive.append(-i)
    return negetive
print(negetive_list(a))