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