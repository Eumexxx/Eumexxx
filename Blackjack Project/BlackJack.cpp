#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;

enum Suit { Hearts, Diamonds, Clubs, Spades };
const vector<string> SuitNames = { "Hearts", "Diamonds", "Clubs", "Spades" };
const vector<string> RankNames = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
const vector<int> RankValues = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 };

struct Card {
    int rank;
    Suit suit;
};

class Deck {
private:
    vector<Card> cards;
public:
    Deck() {
        for (int suit = Hearts; suit <= Spades; ++suit) {
            for (int rank = 0; rank < RankValues.size(); ++rank) {
                cards.push_back(Card{ rank, static_cast<Suit>(suit) });
            }
        }
        shuffle();
    }

    void shuffle() {
        srand(static_cast<unsigned int>(time(0)));
        std::random_shuffle(cards.begin(), cards.end());
    }

    Card deal() {
        Card dealtCard = cards.back();
        cards.pop_back();
        return dealtCard;
    }
};

int getHandValue(const vector<Card>& hand) {
    int value = 0;
    int aces = 0;
    for (const Card& card : hand) {
        value += RankValues[card.rank];
        if (RankNames[card.rank] == "A") {
            aces++;
        }
    }
    while (value > 21 && aces > 0) {
        value -= 10;
        aces--;
    }
    return value;
}

void printHand(const vector<Card>& hand) {
    for (const Card& card : hand) {
        cout << RankNames[card.rank] << " of " << SuitNames[card.suit] << ", ";
    }
    cout << "Value: " << getHandValue(hand) << endl;
}

bool playerTurn(Deck& deck, vector<Card>& playerHand) {
    char choice;
    while (true) {
        cout << "Your hand: ";
        printHand(playerHand);
        cout << "Do you want to (h)it or (s)tand? ";
        cin >> choice;
        if (choice == 'h') {
            playerHand.push_back(deck.deal());
            if (getHandValue(playerHand) > 21) {
                cout << "You bust!" << endl;
                return false;
            }
        } else if (choice == 's') {
            return true;
        }
    }
}

void aiTurn(Deck& deck, vector<Card>& aiHand) {
    while (getHandValue(aiHand) < 17) {
        aiHand.push_back(deck.deal());
    }
    cout << "AI's hand: ";
    printHand(aiHand);
}

void determineWinner(const vector<Card>& playerHand, const vector<Card>& aiHand) {
    int playerValue = getHandValue(playerHand);
    int aiValue = getHandValue(aiHand);

    cout << "Your final hand: ";
    printHand(playerHand);
    cout << "AI's final hand: ";
    printHand(aiHand);

    if (playerValue > 21) {
        cout << "You bust! AI wins." << endl;
    } else if (aiValue > 21 || playerValue > aiValue) {
        cout << "You win!" << endl;
    } else if (playerValue < aiValue) {
        cout << "AI wins." << endl;
    } else {
        cout << "It's a tie!" << endl;
    }
}

int main() {
    Deck deck;
    vector<Card> playerHand;
    vector<Card> aiHand;

    playerHand.push_back(deck.deal());
    playerHand.push_back(deck.deal());
    aiHand.push_back(deck.deal());
    aiHand.push_back(deck.deal());

    if (playerTurn(deck, playerHand)) {
        aiTurn(deck, aiHand);
    }

    determineWinner(playerHand, aiHand);

    return 0;
}