# OOB -- object oriented programming
# it is style to write and manage our programes
# here we will study about class,object(instance) and method
# class is a blueprint
# _init_ method is also known as constructor
# method -- any function define under a class is known as method
# self represent object
class Person:
    def __init__(self,f_name,l_name,age):
        print("init method get called")
        self.f_name = f_name #instance variable
        self.l_name = l_name #instance variable
        self.age = age #instance variable
    def full_name(self):#instance method
        return f"{self.f_name} {self.l_name}"
    def is_above_18(self):#instance method
        return self.age>18
p1 = Person("harshit", "tiwari", 24) #object
p2 = Person("harsh", "tari", 24) #object
p3 = Person("arshit", "tiwari", 24) #object
print(p1.f_name)
print(p2.f_name)
print(p3.f_name)
print(p2.full_name())
print(p1.is_above_18())