import useful_tools

# Advanced guessing game

correct_guess = "antelope"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != correct_guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")


i = 1
while i <= 5:
    print(i)
    i += 1

# for loops
for letter in "life":
    print(letter)

friends = ["Sam", "Jamo", "Alpha", "Kim", "Stevo"]
for friend in friends:
    print(friend)


for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
'''
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
'''

#print(raise_to_power(2,4))
print(useful_tools.raise_to_power(3,3))

#Translation app
#Translate all vowels to letter 'g'
'''
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
'''
# print(translate(input("Enter a phrase: ")))
print(useful_tools.translate(input("Enter phrase: ")))

#

for friend in useful_tools.theoffice:
    print(friend)
