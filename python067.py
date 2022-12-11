# class Students:
#     def __init__ (self,name,rollNo):
#         self.name = name
#         self.rollNo = rollNo
#     def info(self):
#         print("name is : ",self.name,"and rollno is : ",self.rollNo)
# student1 = Students("kriti","08")
# student2 = Students("kavya","03")
# student1.info()
# student2.info()
# print(id(student1)) #the memory where these types of id is created is known as heap memory
# print(id(student2))



# class Person:
#     def __init__(self):
#         self.name = "kriti"
#         self.number = "42"
#     def compare(self,other):
#         if (self.number == other.number):
#             return True
#         else:
#             return False
# p1 = Person()
# p2 = Person()
# p2.number = 18
# if p1.compare(p2):
#     print("same")
# else:
#     print("different")
# print(p1.name)
# print(p2.name)
""" instance variables - value varies from obj to obj"""

class Car:
    wheel = 4
    def __init__(self):
        self.company = "BMW"
        self.mileage = 10
car1 = Car()
car2 = Car()
Car.wheel = 5
print(car1.mileage,car1.wheel)
print(car2.mileage)