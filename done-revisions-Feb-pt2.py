#Determine whether a number is a prime number
num = int(input("Enter the number to check for Prime:"))
flag = False

if num > 1:
    for i in range(2, num):
        if num%i == 0:
            flag = True
            print("{0} is NOT prime!".format(num))
            break
        else:
            print("{0} is a PRIME!".format(num))
#elif num == 1:
#    print("{0} is PRIME".format(num))