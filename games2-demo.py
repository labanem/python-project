i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Done with the loop")

# Guessing game
#secret_word = "monopoly"
#guess = ""
#while guess != secret_word:
#    guess = input("Enter guess: ")
#print("You won!")

# Advanced guessing game

correct_guess = "antelope"
guess = ""
guess_count = 0
guess_limit = 3

while guess != correct_guess and guess_limit != 3:
    if guess_count <= guess_limit and guess != correct_guess:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        print("We won!")