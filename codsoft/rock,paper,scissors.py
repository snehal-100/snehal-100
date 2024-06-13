import random


print("Welcome to the Rock , Paper and Scissors Game")
print("INSTRUCTIONS/RULES: \na)Rock Beats Scissors \nb)Scissors Beats Paper \nc)Paper Beats Rock")

while True:
    print("What you want to choice: \n1.Rock \n2.Scissors \n3.paper")
    n = int(input("Enter your choice:"))

    if n == 1:
        print("You choose Rock")
    elif n == 2:
        print("You choose Scissors")
    elif n == 3:
        print("You choose Paper")
    else:
        print("Not a valid choice.")

    m = random.randint(1,3)
    if n<=3 and n>=1:
        print("Computer choose:")
        if m == 1:
            print("Computer choose Rock")
        elif m == 2:
            print("Computer choose Scissors")
        elif m == 3:
            print("Computer choose Paper")

    else:
        print("Game is terminated")

    if n == 1 and m == 2:
        print("You won")
    elif n == 1 and m == 3:
        print("You lost")
    elif n == 2 and m == 1:
        print("You lost")
    elif n == 2 and m == 3:
        print("You won")
    elif n == 3 and m == 1:
        print("You lost")
    elif n == 3 and m == 2:
        print("You won")
    else:
        print("Match Tied")

    o = input("Are you willing to play again?")
    if o == 'no':
        print("Thank you for playing")
        break
