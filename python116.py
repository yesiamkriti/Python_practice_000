# kwargs (keyword argument)
# **kwargs (double star operator)
# kwargs as a parameter
# ** means dicitionary converter
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")
func(first_name = "Harshit",last_name = "Kumar")
# dicitionary unpacking
def student(**name):
    for i,j in name.items():
        print(f"{i}:{j}")
dict = {"name":"Abhijeet", "age":"11","class":"7"}
student(**dict)