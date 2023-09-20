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