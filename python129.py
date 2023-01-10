# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size=="S":
    rs1=15
elif size=="M":
    rs1=20
else:
    rs1=25
if add_pepperoni=="Y"and size=="S":
    rs2=rs1+2
elif (add_pepperoni=="Y") and (size=="L"or"M"):
    rs2=rs1+3
else:
    rs2=rs1
if extra_cheese=="Y":
    print(f"Your final bill is: ${rs2+1}.")
else:
    print(f"Your final bill is: ${rs2}.")