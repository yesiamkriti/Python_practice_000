# define a function which will take list as a argument and this function
# will return a reversed list
# examples
# [1,2,3,4]------> [4,3,2,1]
# ['word1','word2']------> ['word2','word1']

# note you simply do this with reverse method or [::-1]
# but try to do this with append and pop method
def reverse_list(l):
    empty=[]

    # l.reverse()
    # return l

    # return l[::-1]

    for x in range(len(l)):
        empty.append(l.pop())
    return empty
l=list(input("enter the items of list : ").split(','))
print(reverse_list(l) )
