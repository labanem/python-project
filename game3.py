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
    i = i + 1