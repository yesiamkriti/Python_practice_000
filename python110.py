class person:
    def __init__(self):
        self.firstname =input()
        self.lastname = input()
    def printname(self):
        print(self.firstname + " " + self.lastname)
class student(person):
    pass
x=student()
x.printname()