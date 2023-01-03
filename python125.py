# any and all function
number1 = [2,4,6,8,88]
number2 = [5,40,36,15,81,78,92,88]

# use of all function
print(all(num%2==0 for num in number1))
# use of  any function
print(any(num%2!=0 for num in number1))