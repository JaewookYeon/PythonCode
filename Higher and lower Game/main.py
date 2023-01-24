import art
import random
import game_data
print(art.logo)


def get_random_account():
    return random.choice(game_data.data)


def compare_followers(FirstOne, SecondOne):
    Ffollowers = FirstOne["follower_count"]
    Sfollowers = SecondOne["follower_count"]
    if Ffollowers > Sfollowers:
        return 'A'
    else:
        return 'B'


def game():
    is_game_over = False
    score = 0

    FirstOne = get_random_account()
    SecondOne = get_random_account()

    while not is_game_over:
        while FirstOne == SecondOne:
            SecondOne = get_random_account()
        print(f'Compare A: {FirstOne["name"]}, {FirstOne["description"]}, from {FirstOne["country"]}')
        print(art.vs)
        print(f'Against Compare B: {SecondOne["name"]}, {SecondOne["description"]}, from {SecondOne["country"]}')
        result = compare_followers(FirstOne, SecondOne)

        choice = input('Who has more followers? : ')

        if choice == compare_followers(FirstOne, SecondOne):
            score += 1
            print(f'You are right! Current score: {score}')
        else:
            print(f'''Sorry that's wrong. Final score: {score}''')
            is_game_over = True

game()