import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = EASY_LEVEL_ATTEMPTS
    elif difficulty == 'hard':
        attempts = HARD_LEVEL_ATTEMPTS
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        attempts = EASY_LEVEL_ATTEMPTS
    return attempts

attempts = set_difficulty()

number_to_guess = random.randint(1, 100)
#print(number_to_guess)

while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

    if guess < number_to_guess:
        print("Too low. Try again.")
    elif guess > number_to_guess:
        print("Too high. Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
        break
    attempts -= 1
else:
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

