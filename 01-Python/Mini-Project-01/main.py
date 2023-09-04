# Mohamed Rezq
# Mini-Project:
# ➔ Ask the user to enter a command "add","sub","mult","div"
# and two # numbers to simulate a calculator.
# All of your functions are in a separate script calc.py
# Your main code is in main.py

from calc import *

# session status
session = True

# start the program
while(session):
    operation = input("Select operation (add/sub/mult/div): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if(operation == "add"):
        result = add(num1, num2)
    elif(operation == "sub"):
        result = sub(num1, num2)
    elif(operation == "mult"):
        result = mult(num1, num2)
    elif(operation == "div"):
        result = div(num1, num2)
    else:
        print("Wrong operation, please select only allowed operations")
        continue
    print(f"{num1} {operation} {num2} = {result}")
    session = int(input("Do you want to continue? (1: Yes / 0: No): "))
