#create a function to print your name and age
def myfun(name,age ):
   print("name:"+name +" age:"+ age)
myfun("kriti", "19")
# write a program to create a function using following condition
#it should accept employer name and salary both
#if the salary is missing then assign the default as 10000 to salary
#Ben(12000) mike(15000) bob()
def employer(Name,Salary = "10000"):
    print(" Name: "+ Name + " Salary: " + Salary)
employer(" Ben " ,"12000")
employer(" Mike ", "15000")
employer(" Bob ")
#we will study recursion in next class