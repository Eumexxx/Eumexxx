
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []
        # Create a deck of cards by iterating through ranks and suits
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(rank, suit))
        self.shuffle()  # Shuffle the deck when initialized

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffle the deck

    def deal(self):
        return self.cards.pop()  # Deal a card from the top of the deck

def get_hand_value(hand):
    value = 0
    aces = 0
    # Calculate the total value of the hand, accounting for Aces
    for card in hand:
        if card.rank.isdigit():
            value += int(card.rank)
        elif card.rank in ["J", "Q", "K"]:
            value += 10
        elif card.rank == "A":
            value += 11
            aces += 1
    # Adjust for Aces if the total value exceeds 21
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def print_hand(hand):
    # Print each card in the hand and its value
    for card in hand:
        print(f"{card.rank} of {card.suit}, ", end="")
    print(f"Value: {get_hand_value(hand)}")

def player_turn(deck, player_hand):
    while True:
        print("Your hand: ", end="")
        print_hand(player_hand)
        choice = input("Do you want to (h)it or (s)tand? ")
        if choice == 'h':
            player_hand.append(deck.deal())  # Deal a card to the player
            if get_hand_value(player_hand) > 21:
                print("You bust!")  # Inform the player if they bust
                return False
        elif choice == 's':
            return True  # Player stands

def ai_turn(deck, ai_hand):
    # AI hits until hand value is 17 or higher
    while get_hand_value(ai_hand) < 17:
        ai_hand.append(deck.deal())  # Deal a card to the AI
    print("AI's hand: ", end="")
    print_hand(ai_hand)

def determine_winner(player_hand, ai_hand):
    player_value = get_hand_value(player_hand)
    ai_value = get_hand_value(ai_hand)

    # Print the final hands of the player and AI
    print("Your final hand: ", end="")
    print_hand(player_hand)
    print("AI's final hand: ", end="")
    print_hand(ai_hand)

    # Determine the winner based on hand values
    if player_value > 21:
        print("You bust! AI wins.")
    elif ai_value > 21 or player_value > ai_value:
        print("You win!")
    elif player_value < ai_value:
        print("AI wins.")
    else:
        print("It's a tie!")

def main():
    deck = Deck()  # Initialize the deck
    player_hand = [deck.deal(), deck.deal()]  # Deal initial cards to the player
    ai_hand = [deck.deal(), deck.deal()]  # Deal initial cards to the AI

    if player_turn(deck, player_hand):  # Player's turn
        ai_turn(deck, ai_hand)  # AI's turn

    determine_winner(player_hand, ai_hand)  # Determine the winner

if __name__ == "__main__":
    main()  # Run the game
