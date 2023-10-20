from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_GCD, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import launches_game


def gives_answer(first_num, second_num):
    max_num = max(first_num, second_num)
    min_num = min(first_num, second_num)

    while max_num % min_num != 0:
        max_num, min_num = min_num, max_num % min_num
    return min_num


def build_logic():
    '''Logic for finding the greatest common divisor'''

    first_num = make_num(START_OF_RANGE, END_OF_RANGE)
    second_num = make_num(START_OF_RANGE, END_OF_RANGE)

    task = f'{first_num} {second_num}'
    correct_answer = gives_answer(first_num, second_num)

    return str(correct_answer), task


def starts_brain_gcd():
    launches_game(build_logic, QUESTION_BRAIN_GCD)
