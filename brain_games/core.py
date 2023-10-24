import prompt
from brain_games.constant import NUMBER_OF_ROUNDS


def start_game(get_answer_task, welcome_game):
    '''Game framework function, responsible
    for the general logic of games'''

    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name? ')
    print(f'Hello, {user_name}!\n{welcome_game}')

    for _ in range(NUMBER_OF_ROUNDS):

        correct_answer, task = get_answer_task()
        user_answer = prompt.string(f'Question: {task}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f'"{user_answer}" is wrong answer ;(.'
                         f'Correct answer was "{correct_answer}" '
                         f"Let's try again, {user_name}!")
        print(f'Congratulations, {user_name}!')
