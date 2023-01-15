import random

import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = cards[random.choice(cards)]
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.apprend(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print(f'Draw {user_score} {computer_score}')
    elif user_score > 21:
        print(f'You lose {user_score} {computer_score}')
    elif computer_score == 0:
        print('You lose Computer has Blackjack')
    elif user_score == 0:
        print('You win You have Blackjack')
    elif computer_score > 21:
        print(f'You win {user_score} {computer_score}')
    elif user_score > computer_score:
        print(f'You win {user_score} {computer_score}')
    else:
        print(f'You lose {user_score} {computer_score}')


def play_game():
    print(art.logo)
    user_card = []
    com_card = []

    for i in range(2):
        user_card.append(deal_card())
        com_card.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_card)
        com_score = calculate_score(com_card)
        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {com_card[0]}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input('''Type 'y' to get another card, type  'n' to pass: ''') == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    while com_score < 17:
        com_card.append(deal_card())
        com_score = calculate_score(com_card)
    print(f"   Your final cards: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {com_card}, final score: {com_score}")
    compare(user_score, com_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
