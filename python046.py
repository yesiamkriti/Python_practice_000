# ask user to input 3 numbers and you hav e to print average of threee numbers using strinh formatting
# bonus :- try to take all three comma seperated inputs in one line
# taking input in one line
a,b,c= input("enter three number: ").split(",")
print(f"average of three numbers is :{(int(a) + int(b) + int(c))/3}")