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
