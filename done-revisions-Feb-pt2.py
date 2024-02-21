#Classes and Objects
from Student import person
from Student import graduate

person1 = person("Marcus",14,"male","black",6.0,112,3.7)
person2 = person("Wincate", 21, "female", "Asian",6.1, 87,4.0)
person3 = person("Loki",322,"Male","alien",6.7,92,4.2)

print(person1.gender)
print(person1.education_level())

print(person2.race)
print(person2.education_level())

print(person3.education_level())