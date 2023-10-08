from brain_games.random_num import make_num


def build_logic():
    '''Game logic brain-prime'''

    random_num = make_num()
    task = random_num

    correct_answer = 'yes'
    for i in range(2, random_num // 2 + 1):
        if random_num % i == 0:
            correct_answer = 'no'
    if random_num == 1:
        correct_answer = 'no'

    return correct_answer, task
