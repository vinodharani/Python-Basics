secret_word = "giraffe"
guess_count = 0
guess_limit = 3
are_guesses_left = True
guess = ""

while secret_word != guess and are_guesses_left:
    if guess_count < guess_limit:
        guess_count += 1
        guess = input("Enter your guess #" + str(guess_count) + ":" )
    else:
        are_guesses_left = False

if not are_guesses_left:
    print("You are out of guesses, YOU LOSE")

print("You guessed it right")
print("No of guesses: " + str(guess_count))
