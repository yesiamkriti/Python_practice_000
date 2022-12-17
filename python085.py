#  Sat Dec 17 2022 12:51:40 GMT+0530 (India Standard Time)
class students:
    collegeName = "LPU" #static variable
    def __init__(self,python,web,maths):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = maths
    def average(self):
        return(self.subject1 + self.subject2 + self.subject3)/3
    # def get_subject1(self):
    #     return self.subject1 #accessor
    # def set_marks(self,value):
    #     self.subject1 = value # mutator
    @classmethod
    def collegeDetail(cls):
        return cls.collegeName

    @staticmethod
    def staticMethod():
        print("This is a method")
student1 = students(45,55,65)
student2 = students(12,54,24)
print(student1.average())
print(student2.average())
print(students.collegeDetail())
#mutator and accessor
#instanse variable 
#
