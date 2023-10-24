from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_GCD, \
    START_OF_RANGE, END_OF_RANGE
from brain_games.core import start_game
import math


def get_answer(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_answer_task():
    '''Logic for finding the greatest common divisor'''

    first_num = make_num(START_OF_RANGE, END_OF_RANGE)
    second_num = make_num(START_OF_RANGE, END_OF_RANGE)

    task = f'{first_num} {second_num}'
    correct_answer = get_answer(first_num, second_num)

    return str(correct_answer), task


def start_gcd():
    start_game(get_answer_task, QUESTION_BRAIN_GCD)
