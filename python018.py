import random
User_input = input("Enter your choice:(paper,rock,scissor)")
possible_actions = ["paper","rock","scissor"]
computer_actions = random.choice(possible_actions)
# print user action and computer action
if User_input == computer_actions :
    print("!!!---Tie---!!!")
print("the action of computer is:", computer_actions)
if (User_input == "rock") and (computer_actions == "paper"):
    print("paper the winner is computer ...congratulation!!...")
if (User_input == "rock") and (computer_actions == "scissor"):
    print("rock and the winner is user...congratulations!!...")
if (User_input == "scissor") and (computer_actions == "rock" ):
     print("rock and the winner is computer...congratulations!!...")
if (User_input == "scissor") and (computer_actions == "paper"):
     print("scissor and the winner is user...congratulations!!...")
if (User_input == "paper") and (computer_actions == "rock"):
     print("paper and the winner is user...congratulations!!...")
if (User_input == "paper") and (computer_actions == "scissor"):
     print("scissor and the winner is computer...congratulations!!...")


