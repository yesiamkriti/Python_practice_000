# dictionary comprehension
# we have to print {1: "odd",2:"even"}
odd_number = {i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(odd_number)