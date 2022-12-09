"""Accept a number from the user 
calculate and print the sum of all the numbers
from 1 to input
using for loop"""
number =int(input("Give a number:"))
start = 0
for i in range(0,number + 1):
    start += i
print(start)
"""list: it is a non homogeneous data structure that stores elements in single row and multiple row and coloums
representation []
example : [1,2,3]
it allow dublicate copy
list[] function
mutable
ordered

tuple : it is a non homogeneous data structure that store elements in single row and multiple row/columns
representation ()
example : (1,2,3)
it allow dublicate copy
tuple() function
immutable
ordered

set : non homogeneous but stores in single row
representation {}
example : {1,2,3}
it doesn't allow dublicate copy
set() function
mutable but elements are not dublicated
unordered

dictionary : non homogeneous which store key value pairs
representation {}
example : {1,2,3}
it doesn't allow dublicate keys
dic() function
mutable but keys are not dublicated
ordered
"""