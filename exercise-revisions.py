# Qn 18
def num(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num += 1
        print("\r")

n = 5
num(5)

# Qn 19

alphabet = [ "A", "B", "C", "D", "E"]

def display_alphabet(alphabet):
    for i in range(len(alphabet)):
        for j in range(0,i+1):
            print(alphabet[i],end=" ")
        print("\r")
         
display_alphabet(alphabet)

#Qn 19 using ASCII

def num(n):
    num = 65
    for i in range(0,n):
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
            num += 1
        print("\r")

n = 5
num(n)

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            # (Fill in the missing line here)
            max_num = num
    return max_num

nums = [176,3,4,6,3]
print(find_max(nums))