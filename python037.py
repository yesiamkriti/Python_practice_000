"""tupples store multiple items in a  single variable
1) ordered
2)unchangeable
3)use () for tupple
4) allow dublicate copy"""
fruits = ('apple','mango','papaya','cherry','banana',12,True,'mpple')
print(fruits)
print(len(fruits))
print(fruits[4])
print(fruits[-1])
print(fruits[0:])
print()
veg = ("brinjal",)
print(veg)
fruits1 = [fruits] # typecast using square bracket
print(fruits1)
fruits2 = list(fruits) # typecast using list function
print(fruits2)
fruits2.append('berry')
print(fruits2)
fruits2.extend(fruits)
print(fruits2)
#reverse the above tuple
print(fruits[::-1])
name = ("kriti",)
print(name)