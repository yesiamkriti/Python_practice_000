class A: #parent class or supper class
    def __init__(self):
        print("Init of class A")
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")
class B(): #child class 
    def __init__(self):
        print("Init of class B")
    def method3(self):
        print("This is method 3")
    def method4(self):
        print("This is method 4")  
class C(A,B): #child class # if A and B are independent class then we can write as c(a,b)
    def __init__(self):
        super().__init__()
        print("supper of C")
    def method5(self):
        print("This is method 5")
    def method6(self):
        print("This is method6")  
obj = C()