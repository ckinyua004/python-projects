import random

print("Welcome to Rock, paper, scissors game..")

choices = ["Rock", "Paper", "Scissors"]

human_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")
computer_choice = random.choice(choices)

