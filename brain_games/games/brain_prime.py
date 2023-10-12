from brain_games.utils import make_num
from brain_games.constant import BRAIN_PRIME, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import build_game


def gives_answer(random_num):
    correct_answer = 'yes'
    for i in range(2, random_num // 2 + 1):
        if random_num % i == 0:
            correct_answer = 'no'
    if random_num == 1:
        correct_answer = 'no'
    return correct_answer


def build_logic():
    '''Game logic brain-prime'''

    random_num = make_num(START_OF_RANGE, END_OF_RANGE)
    task = random_num
    correct_answer = gives_answer(random_num)
    return correct_answer, task


def starts_the_game():
    build_game(build_logic, BRAIN_PRIME)
