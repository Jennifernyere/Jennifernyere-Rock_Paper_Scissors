import random

choices = ["R", "P", "S"]
#where R = rock, P = paper and S = scissors

while True:
    player = input("Pick an option: R, P, or S ").upper()
    computer = random.choice(choices)
    print("User: " + player)
    print("Computer:" + computer)

    if player not in choices:
        print("please pick a valid option, thank you")
        continue

    if player == "r" and computer == "s":
        print("You win!")
    elif player == "p" and computer == "r":
        print("You win!")
    elif player == "s" and computer == "p":
        print("You win!")
    elif player == computer:
        print("Tie")
        continue
    else:
        print("The computer wins!")
        break
    
print("Goodbye!!")

