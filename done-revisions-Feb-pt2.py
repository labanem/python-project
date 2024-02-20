#Determine if a number is an Odd or Even number
try:
    num = float(input("Enter number: "))

    if num%2 == 0:
        print("{0} is an EVEN number.".format(num))
    else:
        print("{0} is an ODD number.".format(num))
except ValueError as err:
    print(err)
