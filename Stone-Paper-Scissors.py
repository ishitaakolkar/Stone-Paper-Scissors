import random

print("Welcome to Stone, Paper, Scissors! \nPress 1 for stone\n2 for paper\n3 for scissors")

x = int(input('Choose your character: '))
y = random.randint(1, 3)

if y == 1:
    print("The computer chose stone.")
elif y == 2:
    print("The computer chose paper.")
else:
    print("The computer chose scissors.")

if x == y:
    print("It's a draw!")
elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
    print("You lose!")
elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
    print("You win!")
else:
    print("Invalid input!")
