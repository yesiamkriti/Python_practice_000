# input = [1,2,3,4,5,6,7,8,9]
# output = [-1,2,-3,8,-5,12,-7,16,-9]
# use condition comprehension 

# normal
l = []
def list1(l):
    for i in range(1,11):
        if i%2==0:
            l.append(i*2)
        else:
            l.append(-i)
    print(l)
list1(l)

# comprehension
def list2():
    return[i*2 if i%2==0 else -i for i in range(1,11)]
print(list2())