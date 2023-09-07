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

#Writing and appending a file
try:
#    employee_file = open("c:\\Users\\Lambs\\git\\python-project\\employees.txt", "r")
    employee_file = open(r"c:\Users\Lambs\git\python-project\employees1.txt", "w")

    print(employee_file.write("\nKevin - Accountant"))

    employee_file.close()

except FileNotFoundError as err:
    print(err)


# Reading a file
try:
#    employee_file = open("c:\\Users\\Lambs\\git\\python-project\\employees.txt", "r")
    employee_file = open(r"c:\Users\Lambs\git\python-project\employees1.txt", "r")

    for employee in employee_file.readlines():
        print(employee)

    employee_file.close()

except FileNotFoundError as err:
    print(err)