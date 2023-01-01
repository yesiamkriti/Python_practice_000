# def func(l):
#     # if l%2==0:
#     #     return True
#     # else:
#         # return False #same

#     # if l%2==0:
#     #     return True
#     # return False  # same

#     return l%2==0  #same
# l = int(input("enter a number : "))
# print(func(l))

# # by using lambda function

# print(lambda s : l%2==0)

# # use of if and else in lambda 
p=(lambda s : True if len(s)>5 else False)
print()
# #  noramaly
def func2(t):
    if len(t)>5:
        return True
    return False
print(func2("hugyss"))
