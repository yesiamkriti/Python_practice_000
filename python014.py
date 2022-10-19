#take a string af length 5 [index 0-4]
#print first charter
#print middle charter
#print last charter
a = "kriti"
print(a[0])
b = len(a) // 2
print(a[b])
print(a[4])
#global variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
#one more way to write global variable
# we can write global in global variable
print("Python is " + x)
def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)
