import prompt
from brain_games.constant import RIGHT_ANSWERS


def greets_user(welcome_game):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!')
    print(welcome_game)
    return name


def build_game(game_logic, welcome_game):
    '''Game framework function, responsible
    for the general logic of games'''

    user_name = greets_user(welcome_game)

    for _ in range(RIGHT_ANSWERS):

        correct_answer, task = game_logic()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}" '
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
