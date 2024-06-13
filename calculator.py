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

