#A company decided to give bones of rs 1000 to employee, if his/ her service is more than 5 years.
# Ask the employee about its salary and year of experience  and print the net bonus amount
year =float(input("Enter your experience year :"))
if year > 5 :
    salary = float(input("Enter your salary:"))
    bonus = 1000
    total_salary = salary + bonus
    print("after bonus, the net salary is:",total_salary)
else:
    print("sorry!! no bonus because your experience year is less than 5 years")