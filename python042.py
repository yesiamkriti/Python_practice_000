# ask the user to input a number containing more than one digit 
# e.g = 123456...n 
# calculate 1+2+3+4+5+6+....n  and print
n=str(input())
total=0
i=0
while i < len(n):
    total+=int(n[i])
    i+=1
print(total)
