# conditional comprehension
# if we have to print even no 

list1 = []
for i in range(0,11):
    if i%2==0:
        list1.append(i)
print(list1)

print([i for i in range(0,11) if i%2==0])