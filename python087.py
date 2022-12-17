#Polymorphism means many form
print(len("Hello"))
print(len([10,20,30]))

def add(x,y,z):
    return (x+y+z)
print(add(3,4,5))

class India:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("English")
    def Type(self):
        print("undeveloped")
class USA:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def Type(self):
        print("developed")
obj1 = India()
obj2 = USA()

for i in (obj1,obj2):
    i.capital()
    i.language()
    i.Type()

class Bird:
    def character(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
class Sparrow(Bird):
    def fly(self):
        print("sparrow can fly")
class Ostrich:
    def fly(self):
        print("Ostrich cannot fly")
Bird1 = Bird()
Bird2 = Sparrow()
Bird3 = Ostrich()
Bird1.eyes()
Bird1.fly()
Bird2.fly()
Bird3.fly()