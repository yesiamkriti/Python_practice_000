#random number
import random
print(random.randrange(1,6))
#array: multiple value which we can store in a variable
string = "ABCD"
print(string[2])
print(len(string))
a = "          HELLO WORLD"
b = "Hello"
c = "World"
d = b + c
print(d)
print(a[8:11])
print(a[-1])
print(a[:7])
print(a[7:])
print(a[-4:-1])
print(len(a))
#upper and lowercase
print(a.lower())
#strip is used to remove unwanted space
print(a)
print(a.strip())
#replace
print(a.replace("HELLO","Hey"))
#in
Chilu = "A quick brown fox jump over the lazy dog"
if "quick" in Chilu:
    print("Yes")
else:
    print("no")
#not in
if "quick" not in Chilu:
    print("Yes")
else:
    print("no")
#string array
a = "I LOVE MY INDIA"
print(a[0])
#looping through string
for x in "love u":
    print(x)
#string length
print(len(a))
#check string
print("LOVE" in a)
#use of if in checking string
if "LOVE"in a:
 print("yes,LOVE is present")
#checking  not in
print("you" not in a)
#checking if not 
print("no,you are not present.")
#python slicing
print(a[0:5])
#slice from start
print(a[:10])
#slice from end
print(a[2:])
# negetive indexing
print(a[-16:0])
# use of for loop
for i in a:
    print(i)
