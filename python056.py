# filter
list1=[3,4,1.,51,24,54,84,588,15]
even_num = list(filter(lambda i: i%2==0, list1))
print(even_num)
num = list(filter(lambda b: b>5, list1))
print(num)
# map
square_num = list(map(lambda c : c**2,list1))
print(square_num)
list2 = [10,20,30,40,50]
triple_value = list(map(lambda d:d*3, list2))
print((triple_value))
def case(list):
    for a in list:
        if a.islower():
            a=a.upper()
        else:
             a=a.lower()
        return a
list3 = ["a","B","C","D","e","f"]
uppercase = list(map(case,list3))
print(uppercase)
