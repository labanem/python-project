import useful_tools

#Revision 20 Feb 2024
try:
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("Addition: ",useful_tools.addition(int(number1), int(number2)))
except ValueError as err:
    print(err)

#Exponentials of numbers
basenumber = input("Enter base number: ")
powernumber = input("Enter power number: ")

print("Exponential: ",useful_tools.exponential(int(basenumber),int(powernumber)))

#Greatest of 3 numbers
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    if a > b and a > c:
        print("a wins!",a)
    elif b > a and b > c:
        print("b wins!",b)
    else:
        print("c wins!",c)
except ValueError as err:
    print(err)

#Determine if a number is an Odd or Even number
try:
    num = float(input("Enter number: "))

    if num%2 == 0:
        print("{0} is an EVEN number.".format(num))
    else:
        print("{0} is an ODD number.".format(num))
except ValueError as err:
    print(err)

#Determine whether a number is a prime number
num = int(input("Enter the number to check for Prime:"))
flag = False

if num > 1:
    for i in range(2, num):
        if num%i == 0:
            flag = True
            break
if flag:
        print("{0} is NOT prime!".format(num))
else:
    print("{0} is a PRIME!".format(num))