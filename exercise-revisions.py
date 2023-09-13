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