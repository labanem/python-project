#Creating a Student Class

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#Creating a Car Class

class Car:

    def __init__(self, brand, type, colour, is_automatic):
        self.brand = brand
        self.type = type
        self.colour = colour
        self.is_automatic = is_automatic

#Creating a Questions Class

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Chef:
    def makes_mukimo(self):
        print("This chef makes mukimo")

    def makes_pilau(self):
        print("This chef makes pilau")

    def makes_dessert(self):
        print("This chef makes dessert")

class ChineseChef(Chef):

    def makes_pilau(self):
        print("This chef makes mutton biriani")
    
    def makes_fried_rice(self):
        print("This chef makes fried rice")

#Classes Revisions
class Book:
    def __init__(self, title, author, publisher, is_fiction, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_fiction = is_fiction
        self.pages = pages

    def one_day_read(self):
        if self.pages >= 500:
            return False
        else:
            return True
        
#Inheritance
class ChildrensBook(Book):
    def one_day_read(self):
        if self.pages <= 30:
            return True
        else:
            return False
        
#Multiple questions - revision
class Quiz:
    def __init__(self, task, response):
        self.task = task
        self.response = response

class Paper:
    def __init__(self, weight, colour, source, size):
        self.weight = weight
        self.colour = colour
        self.source = source
        self.size = size

    def for_school(self):
        if self.colour == "white":
            return True
        else:
            return False
        
#Multiple choice quiz - Revision
class Multiple_Questions:
    def __init__(self, querry, response):
        self.querry = querry
        self.response = response


#--------------------------------------------------------------------------------------------------------
#Feb 2024 Revisions
class person:
    def __init__(self,name,age,gender,race,height,weight,gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self. height = height
        self.weight = weight
        self.gpa = gpa

    def education_level(self):
        pass

class graduate(person):
    def education_level(self):
        if self.gpa == 4.2:
            return True
        else:
            return False
