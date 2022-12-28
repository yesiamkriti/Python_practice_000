# num to string 
# define a function 
# examples
# input ----> [True, False,[1,2,3],1,1.0,3]
# output ------> ['1','1.0','3']
def num(l):
    return[str(i) for i in l if type(i) == int or type(i)==float]
print(num([True, False,[1,2,3],1,1.0,3]))


# or


list2=[]
def list1():
    for x in [True, False,[1,2,3],1,1.0,3]:
        if type(x) == int or type(x)==float:
            list2.append(str(x))
    print(list2) 
list1()
# updated