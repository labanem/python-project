import useful_tools

try:
    base_num = input("Enter base number: ")
    power = input("Enter power numer: ")

    print(useful_tools.num_powers(int(base_num), int(power)))
except ValueError as err:
    print(err)