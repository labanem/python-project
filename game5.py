from Student import Student
from Student import Car

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Oscar", "CPA", 4.0, True)

print(student2.is_on_probation)

try:
    for particulars in Student:
        print(particulars)

except TypeError as err:
    print(err)

car1 = Car("BMW", "Sports Utility", "red", True)

print(car1.type)