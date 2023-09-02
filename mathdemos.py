# A basic Calculator

#num1 = input("Please Enter the first Number: ")
#num2 = input("Please Enter 2nd Number: ")

#result = float(num1) / float(num2)
#print(result)

# tuples

coordinates = [(2,3),(3,5),(30,88)]
coordinates[0] = (55,70)
print(coordinates)

# Functions

def say_hi(name, age):
    print("Hello " + name + " you are " + age + ".")

say_hi("Michael", "34")
say_hi("Lambs", "18")

def cube(num):
    return num * num * num

result = cube(5)
print(result)

# A more advanced calculator

def calculator(num1,num2):
    return int(num1) / int(num2)

#num1 = input("Please Enter 1st Number: ")
#num2 = input("Please Enter the 2nd Number: ")

#print(calculator(num1,num2))

# If Statements

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are both male and tall")
elif is_male and not(is_tall):
    print("You are male but not tall")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are neither male nor tall")


# Max Value Function

def max_value(num3, num4, num5):
    if num3 >= num4 and num3 >= num5:
        return num3
    elif num4 >= num3 and num4 >= num5:
        return num4
    else:
        return num5

print(max_value(770,740,377))