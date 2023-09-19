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
