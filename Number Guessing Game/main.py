import random
import art
def play_game(attempt):
    attempts = attempt
    random_num = random.randint(1,100)
    is_game_over = False
    print(f'You have {attempts} attempts remaining to guess the number.')
    while not is_game_over:
        guessed_num = int(input('Make a guess: '))
        if random_num == guessed_num:
            print('You win')
            is_game_over = True
        else :
            attempts = attempts -1
            if attempts > 0:
                print(f'You have {attempts} attempts remaining to guess the number.')
                if random_num >guessed_num:
                    print('Too low')
                elif random_num < guessed_num:
                    print('Too high')
                print('Guess again')
            else:
                if random_num >guessed_num:
                    print('Too low')
                elif random_num < guessed_num:
                    print('Too high')
                print('''You've run out of guesses, you lose.''')
                is_game_over = True
print(art.logo)
print('Welcome to the Number Guessing Game!')
print('''I'm am thinking of a number between 1 and 100.''')
difficulty = input('''Choose a difficulty. Type 'easy' or 'hard': ''')
if difficulty == 'easy':
    play_game(10)

elif difficulty == 'hard':
    play_game(5)


