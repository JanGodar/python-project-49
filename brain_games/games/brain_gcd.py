from brain_games.utils import get_num
from brain_games.constant import QUESTION_GCD_GAME, \
    START_RANGE, END_RANGE
from brain_games.core import start_game
import math


def get_answer(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_answer_task():
    '''Logic for finding the greatest common divisor'''

    first_num = get_num(START_RANGE, END_RANGE)
    second_num = get_num(START_RANGE, END_RANGE)

    task = f'{first_num} {second_num}'
    correct_answer = get_answer(first_num, second_num)

    return str(correct_answer), task


def start_gcd_game():
    start_game(get_answer_task, QUESTION_GCD_GAME)
