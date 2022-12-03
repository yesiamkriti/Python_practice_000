#taking input of different variables at a time
# use of split ... if we write .split() we have to give space after entering 1st input
# if we write .split(",") then we have use comma after each input
name, age, gender = input("Enter yoyr name, age and gender ").split(",")
print(name, age, gender)
print(name)
print(age)
print(gender)