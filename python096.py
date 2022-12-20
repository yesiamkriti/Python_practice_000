s ={'a','b','c'}
if "a" in s :
    print("present")
else:
    print("not present")
# for loop
for item in s :
    print(item)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

#union
# for union we use pipe |
print(s1 | s2)
#intersection
# for intersection we use &
print(s1 & s2)
