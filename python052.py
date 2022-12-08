#set
# strore multiple  values in single variable
# unordered
# unchangeable
# duplicates are not allowed
myset = {"bike","car","boat"}
myset5 = {"apple","mango","banana"}
myset1 = {1,2,3,4}
myset4 = {4,5,6}
myset2 = myset.union(myset1)
myset.add("cycle")
myset.remove("bike")
print(myset)
print(myset2)
print(myset1.union(myset4))
print(myset1.intersection(myset4))
print(myset1.symmetric_difference(myset4))
print(myset1.issuperset(myset4))
myset.symmetric_difference_update(myset5)
print(myset)
