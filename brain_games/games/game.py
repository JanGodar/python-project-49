import prompt
GOOD_DECISION = 3


def engine_game(game_logic, welcome_game):
    '''Game framework function, responsible
    for the general logic of games'''

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(welcome_game())
    good_decision_counter = 0

    while good_decision_counter != GOOD_DECISION:

        correct_answer, task = game_logic()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            good_decision_counter += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}"'
                  f"Let's try again, {user_name}!")
            break

    if good_decision_counter == GOOD_DECISION:    
        print(f'Congratulations, {user_name}!')

