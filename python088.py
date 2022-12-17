# create a car class without any variables and methods
class Car:
    pass


class Vehicles:
    def __init__(self,name,milage):
        self.name = name
        self.milage = milage
class bus(Vehicles):
    pass
obj1 = bus("abc",10)
print(obj1.milage,obj1.name)
