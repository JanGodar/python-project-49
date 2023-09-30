from brain_games.random_num import make_num


def ask():
    '''Returns the game problem of finding the greatest
       common divisor'''

    return 'Find the greatest common divisor of given numbers.'


def build_logic():
    '''Logic for finding the greatest common divisor'''

    first_num = make_num()
    second_num = make_num()

    max_num = max(first_num, second_num)
    min_num = min(first_num, second_num)
    task = f'{max_num} {min_num}'

    while max_num % min_num != 0:
        max_num, min_num = min_num, max_num % min_num
    correct_answer = min_num

    return str(correct_answer), task
