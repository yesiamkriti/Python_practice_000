# list comprehension
# with the help of list comprehension we can create list in one line
# create a list of square from 1 to 10
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

square2 =[i**2 for i in range(1,11)]
print(square2)

negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

neg = [-i for i in range(1,11)]
print(neg)

names = ['Kriti' , 'Abhijeet' , 'Kavya']
name_letter = []
for name in names:
    name_letter.append(name[0])
print(name_letter)