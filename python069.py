def greater(a,b):
    if a>b:
        return a
    return b 
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     if b>c and b>a :
#         return b
#     else:
#         return c
def new_greatest(a,b,c):
    return greater(greater(a,b),c)
a,b,c =input("Enter three numbers using comma : ").split(",")
print(new_greatest(a,b,c))