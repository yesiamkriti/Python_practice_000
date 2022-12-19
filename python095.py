# set data type
# unordered collection of unique items

s = {1,2,3,2}
print(s)
# print(s[2]) indexing is not valid in set
# we can use set as a remove dublicator
s.add(5)
print(s)
s.remove(2)
print(s)
s.discard(3)
print(s)
s1 =s.copy()
print(s1)
s.clear()
print(s)