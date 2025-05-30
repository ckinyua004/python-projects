import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: \n").lower()
print(guess)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder = "_"
print(placeholder)

game_over = False
while not game_over:
    display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
        print("right")
    else:
        display += "_"
        print("wrong")
print(display)
