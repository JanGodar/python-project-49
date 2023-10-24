from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_PRIME, \
    START_OF_RANGE, END_OF_RANGE
from brain_games.core import start_game


def is_prime(random_num):
    if random_num < 2:
        return False
    for i in range(2, int(random_num ** 0.5 + 1)):
        if random_num % i == 0:
            return False
    return True


def get_answer_task():
    '''Game logic brain-prime'''

    random_num = make_num(START_OF_RANGE, END_OF_RANGE)
    task = random_num
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    return correct_answer, task


def start_prime():
    start_game(get_answer_task, QUESTION_BRAIN_PRIME)
