import os

def hit_or_stay():
    # return True: Hit
    # return False: Stay
    while True:
        input_text = input('Would you like to (H)it or (S)tay?').upper()
        if input_text == 'H':
            return True
        elif input_text == 'S':
            return False
        else:
            print('Invalid input. Please select again.')


def start_of_round(player_info):
    print(f'Player: {player_info.name}\t\tCurrent Balance:{player_info.balance}\n')
    while True:
        try:
            input_buf = float(input('Please enter the amount you would like to bet this round: $'))
            if input_buf > player_info.balance:
                print('You cannot exceed the amount you currently have on the table. Try again.')
            else:
                return input_buf
                break
        except:
            print('What you have entered was not a number. Please enter amount again.')


def stay_or_quit():
    # return True: Stay
    # return False: Quit
    while True:
        input_text = input('Would you like to play again? (Y / N)').upper()
        if input_text == 'Y':
            return True
        elif input_text == 'N':
            return False
        else:
            print('Invalid input. Please select again.')


def card_text(input_card):
    suit_list = ['He', 'Sp', 'Cl', 'Di']
    val_list = ['', ' A', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', 'Ja', 'Qu', 'Ki']
    return suit_list[input_card[0]], val_list[input_card[1]]


VERT = u'\u2502'
HORZ = u'\u2500'
UPPER_RIGHT_CORNER = u'\u2510'
UPPER_LEFT_CORNER = u'\u250c'
LOWER_RIGHT_CORNER = u'\u2518'
LOWER_LEFT_CORNER = u'\u2514'


def card_graphic(in_stream, card):
    ret_str = ['', '', '', '']
    suit, val = card_text(card)
    ret_str[0] = in_stream[0] + UPPER_LEFT_CORNER + HORZ + HORZ + HORZ + HORZ + HORZ + UPPER_RIGHT_CORNER + '\t'
    ret_str[1] = in_stream[1] + f'| {suit}  |' + '\t'
    ret_str[2] = in_stream[2] + f'| {val}  |' + '\t'
    ret_str[3] = in_stream[3] + LOWER_LEFT_CORNER + HORZ + HORZ + HORZ + HORZ + HORZ + LOWER_RIGHT_CORNER + '\t'
    return ret_str


def display(player, house):
    _ = os.system('cls')
    # Printing out the house name and current chip balance
    print(UPPER_LEFT_CORNER + '{0:{fill}{align}24}'.format(UPPER_RIGHT_CORNER, fill=HORZ, align='>'))
    text = f'Player: {house.name}'
    print('|' + '{:{fill}{align}23}'.format(text, fill=' ', align='^') + '|')
    text = f'Balance: {house.balance}'
    print('|' + '{0:{fill}{align}23}'.format(text, fill=' ', align='^') + '|')
    print(LOWER_LEFT_CORNER + '{0:{fill}{align}24}'.format(LOWER_RIGHT_CORNER, fill=HORZ, align='>'))

    card_lines = ['', '', '', '']
    for card in house.current_hand:
        card_lines = card_graphic(card_lines, card)
    print(card_lines[0])
    print(card_lines[1])
    print(card_lines[2])
    print(card_lines[3])
    print(f'House Hand Total: {house.hand_total()}')

    print('----------------------------------------------------------------------------')

    card_lines = ['', '', '', '']
    for card in player.current_hand:
        card_lines = card_graphic(card_lines, card)
    print(card_lines[0])
    print(card_lines[1])
    print(card_lines[2])
    print(card_lines[3])
    print(f'Player Hand Total: {player.hand_total()}')

    # Printing out the player name and current chip balance
    print(UPPER_LEFT_CORNER + '{0:{fill}{align}24}'.format(UPPER_RIGHT_CORNER, fill=HORZ, align='>'))
    text = f'Player: {player.name}'
    print('|' + '{:{fill}{align}23}'.format(text, fill=' ', align='^') + '|')
    text = f'Balance: {player.balance}'
    print('|' + '{0:{fill}{align}23}'.format(text, fill=' ', align='^') + '|')
    print(LOWER_LEFT_CORNER + '{0:{fill}{align}24}'.format(LOWER_RIGHT_CORNER, fill=HORZ, align='>'))
