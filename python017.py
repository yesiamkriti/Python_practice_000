""" take user input (string)
if the len of string is greater than 3
add "ing" as a suffix in the original string
else print the same string given by the user"""
a =str(input(""))
y = len(a)
if y > 3:
    print(a + "ing")
else:
    print(a)
x = 10
b = 5
c = 15
d = 20
str ="a = {2}, b = {0}, c = {3},d = {1}"
print(str.format(c,d,b,x))