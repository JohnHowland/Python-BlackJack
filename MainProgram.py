import GameText as cardText
import support
import os

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
        card = self.deck.pop()
        return card
        pass


class Player:
    def __init__(self, name, staring_balance):
        self.name = name
        self.balance = staring_balance
        self.current_hand = []

    def hand_total(self):
        tot = 0
        ace = 0
        card_val = 0
        for item in self.current_hand:
            if item[1] == 1:
                ace += 1
                continue
            elif item[1] > 9:
                card_val = 10
            else:
                card_val = item[1]

            tot += card_val

        for ace_num in range(ace):
            if tot > 10:
                tot += 1
            else:
                tot += 11

        return tot

    def insert_new_card(self, card):
        self.current_hand.append(card)

    def new_game(self):
        self.current_hand = []

if __name__ == '__main__':

    # creating the deck of cards
    deck_list = []
    for i in range(4):
        for j in range(1, 14):
            tup = (i, j)
            deck_list.append(tup)

    # inserting the deck of cards into the new class
    card_deck = Deck(deck_list)

    name = input('Welcome to Python BlackJack!\n'
                 'Please tell me your name: ')
    init_balance = float(input(f'Hello {name}, please tell me your starting balance: $'))
    player = Player(name, init_balance)
    house = Player('Bank', 500)

    _ = os.system('cls')

    game_on = True
    while game_on is True:
        player.new_game()
        house.new_game()

        support.display(player, house)
        betting_value = support.start_of_round(player)

        player.insert_new_card(card_deck.deal())
        player.insert_new_card(card_deck.deal())
        house.insert_new_card(card_deck.deal())
        house.insert_new_card(card_deck.deal())

        support.display(player, house)
        player_hand_value = player.hand_total()

        while support.hit_or_stay():
            player.insert_new_card(card_deck.deal())
            support.display(player, house)
            player_hand_value = player.hand_total()
            if player_hand_value > 21:
                break

        house_hand_value = 0
        if player_hand_value > 20:
            pass
        elif player_hand_value < 21:
            while True:
                house_hand_value = house.hand_total()
                support.display(player, house)

                if house_hand_value > 21:
                    break
                elif house_hand_value > player_hand_value and house_hand_value < 21:
                    break
                else:
                    house.insert_new_card(card_deck.deal())
        else:
            pass

        if player_hand_value == 21:
            player.balance += betting_value
            house.balance -= betting_value
            print('YOU WIN!')
            # player wins
        elif house_hand_value > 21:
            player.balance += betting_value
            house.balance -= betting_value
            print('YOU WIN!')
            # player wins
        elif player_hand_value > 21:
            house.balance += betting_value
            player.balance -= betting_value
            print('HOUSE WINS!')
            # house wins
        else:
            if player_hand_value > house_hand_value:
                player.balance += betting_value
                house.balance -= betting_value
                print('YOU WIN!')
                # player wins
            else:
                house.balance += betting_value
                player.balance -= betting_value
                print('HOUSE WINS!')
                # house wins

        if player.balance == 0:
            print('You ran out of money... so sorry!')
            break

        if not support.stay_or_quit():
            print('Exiting game. Thank you for playing!')
            break

    print(f'{player.name} chip value: {player.balance}')
    print(f'{house.name} chip value: {house.balance}')
