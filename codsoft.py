Task 1 - Simple Calculator

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
print("Choose the mathematical operation you want to perform:\n1.Addition \n2.Subtraction \n3.Division \n4.Multiplication \n5.Modulus \n6.Exponential")
n =  int(input("Enter your choice:"))

if n==1:
    addition = a+b
    print("Addition of the two numbers is:",addition)
elif n==2:
    subtraction = a-b
    print("Subtraction of the two numbers is:",subtraction)
elif n==3:
    division = a/b
    print("Division of the two numbers are:",division)
elif n==4:
    multiplication = a*b
    print("Multiplication of the two numbers are:",multiplication)
elif n==5:
    modulus = a%b
    print("Modulus of the two numbers are:",modulus)
else:
    exponential = a**b
    print("Exponential of the number is:",exponential)
print("Thank you for using the calculator.")


Task 2- Rock,Paper,Scissors

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
