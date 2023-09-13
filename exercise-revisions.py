# 1 A program to print if the given number is odd or even

num = int(input("Enter number: "))

if (num%2) == 0:
    print("Even number")
    print("{0} is an even".format(num))
else:
    print("{0} is an odd number".format(num))

# 2 A program to find if the given number is positive or negative
try:
    num1 = int(input("Please enter number: "))
    if num1 < 0:
        print("{0} is negative".format(num1))
    elif num1 == 0:
        print("Zero")
    else:
        print("{0} is positive".format(num1))
except ValueError as err:
    print(err)

# 3 Sum of two numbers

num2 = int(input("Enter 1st number: "))
num3 = int(input("Enter 2nd number: "))

print(num2 + num3)
