# generators
# generator is an iterator
# create your first generator with generator function 
# 1) generator function
def even_no(n):
    for i in range(0,n+1,2):
            yield i
n=int(input("Enter a no from where you want to print even number : "))
for num in even_no(n):
    print(num)