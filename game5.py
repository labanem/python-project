from Student import Student
from Student import Car
from Student import Question
from Student import Quiz

#Students
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Oscar", "CPA", 4.0, True)

print(student2.is_on_probation)
print(student1.on_honour_roll())

try:
    for particulars in Student:
        print(particulars)

except TypeError as err:
    print(err)

#Cars
car1 = Car("BMW", "Sports Utility", "red", True)

print(car1.type)


#Multiple Choice Questions
question_prompts = [
    "What is your favourite food?\n(a) Mashed Potatoes\n(b) Pilau\n(c) Matoke\n\n",
    "What is your favourite car?\n(a) BMW\n(b) Fuso\n(c) Mercedes\n\n",
    "Which programming language is your favourite?\n(a) Java\n(b) Python\n(c) C++\n\n",
    "What certification are you taking first?\n(a) Oracle DBA\n(b) DevOps Enginner\n(c) MS Azure\n\n"
]

questions = [
    Quiz(question_prompts[0], "a"),
    Quiz(question_prompts[1], "c"),
    Quiz(question_prompts[2], "b"),
    Quiz(question_prompts[3], "b")
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.task)
        if answer == question.response:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct.")

ask_questions(questions)