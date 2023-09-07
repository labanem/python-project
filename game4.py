# Try Exception


try:
#    numresult = 10/0
    result = int(input("Enter number: "))
    print(result)

except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)