colors =["red","green", "red","blue",22,34,56,True,0b100]
players=("dhoni","messi","dravid")
cars=["tata","nano","alto","jeep"]
numbers = [1,2,3,45,6,76,8,9,22]
print(colors[:3])
colors[2] = "green"
print(colors)
# replace 
print(colors)
colors.insert(2,"indigo")
colors.append("bmw")
print(colors)
print(cars)
print(players)
colors.remove("blue")
colors.extend(players)
print(players)
print(colors)
'''colors.pop(1)
print(colors)
#pop removes from  a specific index 
del colors[0]
print(colors)
colors.clear()
print(colors)
for x in range(len(cars)):
     print(cars[x])
while x > len(cars):
    print(cars[x])
    x+=1
[print(x) for x in cars]
newList = []
for i in cars:
    if "a" in i:
        newList.append(i)
print(newList)
#1st x is expression 2nd for item and cars is list and 4th x for condition 
#newList =[x for x in cars if x=="tata"]
newList =[x.upper() for x in cars]
print(newList)
numbers.sort()
print(numbers)
cars.sort(reverse=True)
print(cars)'''
