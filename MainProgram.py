import GameText as cardText

HEART = 0
SPADE = 1
CLUB = 2
DIAMOND = 3


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        pass


class Deck:
    def __init__(self, deck):
        self.deck = deck
        pass

    def shuffle(self):
        for card_num in range(len(self.deck)):
            if card_num % 2 == 0:  # if the card number is even
                self.deck.insert(card_num, self.deck.pop())

        pass

    def deal(self):
        return self.deck.pop()
        pass


class Player:
    def __init__(self, name, staring_balance):
        self.name = name
        self.balance = staring_balance
        pass


# creating the deck of cards
deck_list = []
for i in range(4):
    for j in range(1, 14):
        tup = (i, j)
        deck_list.append(tup)

# inserting the deck of cards into the new class
card_deck = Deck(deck_list)

for item in card_deck.deck:
    print(item)

card_deck.shuffle()

for item in card_deck.deck:
    print(item)

print(cardText.Ace)

# print(card_deck.deal())
