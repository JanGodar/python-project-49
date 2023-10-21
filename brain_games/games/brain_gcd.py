from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_GCD, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import launches_game
import math


def build_logic():
    '''Logic for finding the greatest common divisor'''

    first_num = make_num(START_OF_RANGE, END_OF_RANGE)
    second_num = make_num(START_OF_RANGE, END_OF_RANGE)

    task = f'{first_num} {second_num}'
    correct_answer = math.gcd(first_num, second_num)

    return str(correct_answer), task


def starts_brain_gcd():
    launches_game(build_logic, QUESTION_BRAIN_GCD)
