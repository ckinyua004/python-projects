import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

def deal_card():
    return deck.pop()

def calculate_score(hand):
    score = sum(values[card[0]] for card in hand)
    # Adjust for Aces
    aces = [card for card in hand if card[0] == 'Ace']
    while score > 21 and aces:
        score -= 10
        aces.pop()
    return score

def show_hand(hand, owner, hide_first=False):
    print(f"\n{owner}'s Hand:")
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            print("  [Hidden Card]")
        else:
            print(f"  {card[0]} of {card[1]}")

def play_blackjack():
    global deck
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Player's Turn
    while True:
        show_hand(player_hand, "Player")
        show_hand(dealer_hand, "Dealer", hide_first=True)
        score = calculate_score(player_hand)
        if score > 21:
            print("\nPlayer busts! Dealer wins.")
            return
        choice = input("\nDo you want to [H]it or [S]tand? ").lower()
        if choice == 'h':
            player_hand.append(deal_card())
        else:
            break

    # Dealer's Turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    # Final Results
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    show_hand(player_hand, "Player")
    show_hand(dealer_hand, "Dealer")

    print(f"\nPlayer Score: {player_score} | Dealer Score: {dealer_score}")
    if dealer_score > 21 or player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

while True:
    play_blackjack()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        break
print("Thanks for playing Blackjack!")