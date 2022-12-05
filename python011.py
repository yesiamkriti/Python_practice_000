#company will give bonus on following careteria
#time spent in the company  bonus
#grater than ten years  10%
#more than 6  8%
#less than 6  5%
#ask the salary and time spent from the user 
#print the net bonus amount accordingly
A = int(input("type your experience year for bonus: "))
B = int(input("your current salary :"))
if A > 10:
    C = (10 % B)+(B)
    print("the net SALARY : ", C)
elif A > 6:
    D = (8 % B)+(B)
    print("the net SALARY : ", D)
elif A < 6:
    F = (5 % B)+(B)
    print("the net SALARY : ", F)
else:
    print("sorry! no bonus")