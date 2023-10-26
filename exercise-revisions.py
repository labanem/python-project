import useful_tools
from Student import Paper
from Student import ChineseChef
from Student import Chef
from Student import Multiple_Questions

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

#classes revision
paper1 = Paper(32, "white", "recycled", "a4")
paper2 = Paper(12, "red", "conifer tree", "a1")

print(paper2.source)
print(paper2.for_school())

chef1 = ChineseChef()
chef1.makes_pilau()

chef2 = Chef()
chef2.makes_pilau()

#Multiple choice exam
question1 = Multiple_Questions("What is the colour of the sky?: ", "Blue")

print(question1.querry)

question_list = [
    "What is the colour of the sky?: \n(a) Blue\n(b) Green\n\n",
    "How many seasons are there in a year?: \n(a)One\n(b) Four\n\n",
    "Which one of these is a fruit?: \n(a)Mango\n(b) Chocolate\n\n"
]

questions = [
    Multiple_Questions(question_list[0],"a"),
    Multiple_Questions(question_list[1],"b"),
    Multiple_Questions(question_list[2],"a")
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.querry)
        if answer == question.response:
            score += 1
    return print("You scored",score, "/", len(questions))

ask_questions(questions)
