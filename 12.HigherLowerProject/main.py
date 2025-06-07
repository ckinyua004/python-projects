import random

# Celebrity data: name and their follower count
celebrities = {
    "Kylie Jenner": 233000000,
    "Cristiano Ronaldo": 530000000,
    "Dwayne Johnson": 357000000,
    "Ariana Grande": 289000000,
    "Kim Kardashian": 349000000,
    "Lionel Messi": 440000000
}

def get_celebrity_pair():
    """Randomly select two celebrities from the list."""
    return random.sample(list(celebrities.items()), 2)

def play_game():
    score = 0
    print("Welcome to the Higher or Lower game!")
    
    while True:
        celeb1, followers1 = get_celebrity_pair()[0]
        celeb2, followers2 = get_celebrity_pair()[1]

        print(f"\nWhich celebrity has more followers?")
        print(f"1. {celeb1}")
        print(f"2. {celeb2}")

        guess = input("Enter 1 or 2: ")

        if guess == '1' and followers1 > followers2:
            print(f"Correct! {celeb1} has {followers1} followers vs {celeb2} with {followers2}.")
            score += 1
        elif guess == '2' and followers2 > followers1:
            print(f"Correct! {celeb2} has {followers2} followers vs {celeb1} with {followers1}.")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {celeb1 if followers1 > followers2 else celeb2}.")
            print(f"Game over! Your final score is {score}.")
            break

if __name__ == "__main__":
    play_game()
