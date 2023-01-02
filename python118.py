# we use enumerate function with for loop to track position of our item in iterable
# how we can do this without using enumerate function
names = ["abc","kavya","abhijeet","kriti"]
pos = 0
for name in names:
    print(f"{pos} ooooo) {name}")
    pos += 1
#  with enumerate funtion
for posi, nam in enumerate(names):
    print(f"{posi} ----> {nam}")

# define a function that take two arguments 
# 1.) list containing string 
# 2.) string taht want to find in your list 
# and this function will return the index of string in your list and if string is not present then return -1
def find_pos(l, target):
    for position, namee in enumerate(l):
        if namee == target:
             return position 
        return -1
print(find_pos(names, "Kavya"))