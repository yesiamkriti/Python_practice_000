import random
winning_no = random.randint(0, 10)
guess = 1
no =int(input("guess a number between 1 to 10: "))
game_over = False
while not game_over:
    if no == winning_no:
        print(f"YOU WIN , you guessed this number in {guess}times")
        game_over =True
        guess+=1
    else:
        if no > winning_no:
            print("your guess is TOO HIGH")
            guess+=1
            no =int(input("guess again: "))
        else:
            print("your guess is TOO LOW")
            guess+=1
            no =int(input("guess again: "))
