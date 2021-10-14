"""A number-guessing game."""


'''
1. Asks for the user’s name

2. Greets the user and prompts them to guess a number

3. Cycles through until the user guesses the right number

4. Ends when the user guesses the right number and 

5. Displays the number of guesses that the user made
'''


"""A number-guessing game."""

from random import randint

tries = 0
number = randint(1, 100)

print("Howdy, what's your name?")

name = input("(type in your name) ")

print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Can you guess what the number is?")

while True:
    guess = input("Your guess? ")

    # Make sure the guess is actually a number
    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number, try again.')
        continue

    # Make sure the guess is between 1 and 100
    if guess < 1 and guess > 100:
        print("Please guess a number between 1 and 100")
        continue

    tries += 1  # this is equivalent to `tries = tries + 1`

    if guess < number:
        print("Your guess is too low, try again.")

    elif guess > number:
        print("Your guess is too high, try again.")

    else:
        print(f"Well done, {name}!")
        print(f"You found my number in {tries} tries!")
        break