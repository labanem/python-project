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
