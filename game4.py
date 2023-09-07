# Try Exception

'''
try:
#    numresult = 10/0
    result = int(input("Enter number: "))
    print(result)

except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)

'''

# Reading a file
try:
    employee_file = open("employees.txt","r")

    print(employee_file.readable())

    employee_file.close()

except FileNotFoundError as err:
    print(err)
