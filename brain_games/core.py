import prompt
from brain_games.constant import NUMBER_ROUNDS


def start_game(get_question_and_answer, game_task):
    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name? ')
    print(f'Hello, {user_name}!\n{game_task}')

    for _ in range(NUMBER_ROUNDS):

        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}" '
                  f"Let's try again, {user_name}!")
            return
        print(f'Congratulations, {user_name}!')
