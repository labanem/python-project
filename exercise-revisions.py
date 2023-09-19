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

