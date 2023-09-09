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