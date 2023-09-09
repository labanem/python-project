#Hello World
print("Hello World")

#Drawing a shape
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

#Building a basic calculator
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

try:
    result = float(num1) + float(num2)
    print(result)
except ValueError as err:
    print(err)

#Mad Libs Game
colour = input("Enter colour: ")
pluralnoun = input("Enter a plural noun: ")
celeb = input("Enter Celebrity name: ")

print("Roses are "+ colour + ",\n" + pluralnoun + " are blue,\nI love " + celeb)

#Building a more advanced calculator

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
operator = input("Enter Operator: ")

try:
    if operator == "+":
        result = float(num1) + float(num2)
    elif operator == "-":
        result = float(num1) - float(num2)
    elif operator == "/":
        result = float(num1) / float(num2)
    print("The result is "+ str(result))

except ValueError as err:
        print(err)

except ZeroDivisionError:
    print("A number cannot be divided by 0")

#Advanced Calculator version 2

def calculate(num1,num2,operator):
    if operator != "+" and operator != "-" and operator != "/":
        print(operator + " is not a valid operator.")
        return
    else:
        try:
            if operator == "+":
                return float(num1) + float(num2)
            elif operator == "-":
                return  float(num1) - float(num2)
            elif operator == "/":
                return float(num1) / float(num2)
        except ValueError as err:
            print(err)
        except ZeroDivisionError as err:
            print(err)

num1 = input ("Enter value of num1: ")
operator = input("Enter operator: ")
num2 = input("Enter value of num2: ")

#print(calculate(num1,num2,operator))

print("The answer is: " + str(calculate(num1,num2,operator)))


'''
#To figure out a way to use classes for a calclulator
# Advanced calculator Version 3
from Classrevisions import Calculator

num1 = input("Enter num1: ")
#operator = "+"
num2 = input("Enter num2: ")

valid_operators = [
    "+",
    "-",
    "/",
    "*"
]

calc = Calculator(num1, num2, valid_operators[0])

print(calc.operator)
'''