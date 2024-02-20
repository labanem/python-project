import random

theoffice  = ["Jim", "Pam", "Dwight", "Oscar", "Michael", "Kelly"]

#Translation app
#Translate all vowels to letter 'g'
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#Revision
# The power of a number
def num_powers(num, power_num):
    result = 1
    for index in range(power_num):
        result = result * num
    return result

#------------------------------------------------------------------------------------------------------------
#Revision question
# 20 Feb 2024

#Addition
def addition(num1,num2):
    result = num1 + num2
    return result

#Exponentials
def exponential(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result
