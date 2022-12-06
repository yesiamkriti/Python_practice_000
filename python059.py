# exercise ,number guessing game
# make a variable, like winning_number and assing any number to it.
# ask user to guess a numbaer .
# if user guessed correctly then print you win
# if user didn't guessed correctly then :
#     if user guessed lower than actuall number print too low
#     if user guessed higher than actual number then print too high
winning_number = 5
user_input = int(input("enter a number b/w 1-10: "))
if user_input == winning_number:
    print("YOU WIN!!!!!!")
elif user_input >5 :
    print("TOO HIGH")
else:
    print("TOO LOW")
    