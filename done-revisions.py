import useful_tools
from Student import Book
from Student import ChildrensBook

#Hello World
print("Hello World")

#Drawing a shape
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

#Building a basic calculator
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

try:
    result = float(num1) + float(num2)
    print(result)
except ValueError as err:
    print(err)

#Mad Libs Game
colour = input("Enter colour: ")
pluralnoun = input("Enter a plural noun: ")
celeb = input("Enter Celebrity name: ")

print("Roses are "+ colour + ",\n" + pluralnoun + " are blue,\nI love " + celeb)

#Building a more advanced calculator

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
operator = input("Enter Operator: ")

try:
    if operator == "+":
        result = float(num1) + float(num2)
    elif operator == "-":
        result = float(num1) - float(num2)
    elif operator == "/":
        result = float(num1) / float(num2)
    print("The result is "+ str(result))

except ValueError as err:
        print(err)

except ZeroDivisionError:
    print("A number cannot be divided by 0")

#Advanced Calculator version 2

def calculate(num1,num2,operator):
    if operator != "+" and operator != "-" and operator != "/":
        print(operator + " is not a valid operator.")
        return
    else:
        try:
            if operator == "+":
                return float(num1) + float(num2)
            elif operator == "-":
                return  float(num1) - float(num2)
            elif operator == "/":
                return float(num1) / float(num2)
        except ValueError as err:
            print(err)
        except ZeroDivisionError as err:
            print(err)

num1 = input ("Enter value of num1: ")
operator = input("Enter operator: ")
num2 = input("Enter value of num2: ")

#print(calculate(num1,num2,operator))

print("The answer is: " + str(calculate(num1,num2,operator)))


'''
#To figure out a way to use classes for a calclulator
# Advanced calculator Version 3
from Classrevisions import Calculator

num1 = input("Enter num1: ")
#operator = "+"
num2 = input("Enter num2: ")

valid_operators = [
    "+",
    "-",
    "/",
    "*"
]

calc = Calculator(num1, num2, valid_operators[0])

print(calc.operator)
'''

#Guessing game
#A user has 3 guesses to guess the right thing. If they don't get it correct, the program
#terminates and displays an 'out of guesses' or 'wrong guess' message
#using if, while, for loops

guess = ""
guess_limit = 3
guess_count = 0
correct_guess = "green"
out_of_guess = False

while guess != correct_guess and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, you lose!")
else:
    print("You win!")

# Building a translator
# Take in a string and tranlate all the vowels to a specific letter

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
               translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter phrase: ")))

#Reading and editing a file
#a - append
#r - read
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

# Raising base number to the power of power number
try:
    base_num = input("Enter base number: ")
    power = input("Enter power numer: ")

    print(useful_tools.num_powers(int(base_num), int(power)))
except ValueError as err:
    print(err)


#Classes and Objects - Revision
book1 = Book("Montecristo", "Martin Suter", "No Exit Press", True, 321)
book2 = Book("Win or Die", "Bruce Craven", "Blink Publishing", False, 1500)

print(book1.author)
print(book2.is_fiction)
print("\n")
print(book1.pages, book1.title, book1.one_day_read())
print(book2.one_day_read())

cbook1 = ChildrensBook("Bah Bah Black", "Black Sheep", "Farmes Publishers", True, 31)

print(cbook1.one_day_read())

#Building a Multiple Choice Exam - Revision
from Student import Quiz

my_questions = [
    "Which of the following is not a distribution of Windows OS?\n(a) Windows 10\n(b) Windows XP\n(C) CentOS\n\n",
    "Select the German car brand from the following list:\n(a) Mercedes\n(b) Fiat\n(c) Suzuki\n\n",
    "Which one is not a former president of Kenya?\n(a) Daniel Moi\n(b) Mwai Kibaki\n(c) Mobutu Sesseseko\n\n"
]

questions = [
    Quiz(my_questions[0], "c"),
    Quiz(my_questions[1], "a"),
    Quiz(my_questions[2], "c")
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.task)
        if answer == question.response:
            score += 1
    print(str(score) + "/" + str(len(questions)))

ask_questions(questions)

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

print("Sum is",num2 + num3)

# 4 To find whether a number is a prime number or not

num4 = int(input("Enter number to check: "))
flag = False
if num4 > 1:
    for i in range(2, num4):
        if (num4 % i) == 0:
            flag = True
        break
if flag:
    print("{0} is NOT a prime number.".format(num4))
else:
    print("{0} is a prime number".format(num4))

    # 5 Determine whether a number is a palindrome or not
# ie. Remains the same when the digits are reversed e.g., 16461

# num5 = int(input("Enter numer to check for palindrome: "))
# I'll circle back to this question

# 6 check if a given number is Armstrong or not
#  I'll circle back to this question

# 7 Anagram
# To circle back to it

# 8 To find a maximum of 2 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print("{0} is greater".format(num2))
else:
    print("The numbers are equal")

# 9 To find the minimum of 2 numbers

def minimum(num3, num4):
    if num3 <= num4:
        return num3
    else:
        return num4
    
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a second number: "))

print(minimum(num3,num4), "is the minimum")

# 10 To find a maximum of 3 numbers

largest = ""
def max(a,b,c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(max(a,b,c))

# 11 To find minimum of 3 numbers

def min(d,e,f):
    if (d <= e) and (d <= f):
        lowest = d
    elif (e <= d) and (e <= f):
        lowest = e
    else:
        lowest = f
    return lowest

print(min(20,322,24))

# 12 To find the factorial of a number

num1 = int(input("Enter a number to find its factorial: "))

def findfactorial(num1):
    factorial = 1
    if num1 < 0:
        print("We cannot get factorials of negative integers")
    elif num1 == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1,num1+1):
            factorial = factorial * i
        return factorial

print(findfactorial(num1), "is the factorial of",num1)

# 13 The fibonacci of a number

nterms = int(input("How many terms?: "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive number.")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# 14 the GCD of two numbers
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)

a = 98
b = 56

if(gcd(a,b)):
    print("GCD of",a,"and",b,"is", gcd(a, b))
else:
    print("Not found!")

# 15 A program to print a right-angled triangled image with *
def myfunc(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

n = 5
myfunc(n)

# 16 A program to print a different type of triangle with *s

def myfunc(n):
    k = n - 1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    
n = 5
myfunc(n)

# 17
def num(n):
    num = 1
    for i in range(0,n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")

n = 5
num(n)

#rev 17
def num(n):
    num = 1
    for i in range(0,n):
        num = 1
        for j in range(0,i+1):
            print(num,end=" ")
            num += 1
        print("\r")

n = 6
num(6)

#rev 15

def stars(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")

n = 7
stars(7)