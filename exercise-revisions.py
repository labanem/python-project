#Reading and editing a file

try:
    revision_file = open(r"C:\Users\Lambs\git\python-project\employees.txt", "a")
    print(revision_file.write("\nStanley - Sales and Marketing"))
    revision_file.close()
except FileNotFoundError as err:
    print(err)

try:
    revision_file = open(r"C:\Users\Lambs\git\python-project\employees.txt", "r")

    for employee in revision_file.readlines():
        print(employee)

    revision_file.close()
except FileNotFoundError as err:
    print(err)