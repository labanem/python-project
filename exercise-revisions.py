#Guessing game
#A user has 3 guesses to guess the right thing. If they don't get it correct, the program
#terminates and displays an 'out of guesses' or 'wrong guess' message
#using if, while, for loops

guess = ""
guess_limit = 3
guess_count = 0
correct_guess = "green"
out_of_guess = False

while guess != correct_guess and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, you lose!")
else:
    print("You win!")
