# DRY - don't repeat 
import random
winning_no = random.randint(0, 10)
guess = 1
while True:
    no =int(input("guess a number between 1 to 10: "))
    if no == winning_no:
        print(f"YOU WIN , you guessed this number in {guess}times")
        break
    else:
        if no > winning_no:
            print("your guess is TOO HIGH")
        else:
            print("your guess is TOO LOW")
        guess+=1
        