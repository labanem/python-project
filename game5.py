from Student import Student
from Student import Car
from Student import Question

#Students
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Oscar", "CPA", 4.0, True)

print(student2.is_on_probation)

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
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct.")

ask_questions(questions)