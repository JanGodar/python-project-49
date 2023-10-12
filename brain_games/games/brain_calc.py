from brain_games.utils import make_num
from brain_games.constant import PLUS, MINUS, START_OF_RANGE, \
                                 END_OF_RANGE, BRAIN_CALC
from brain_games.core import build_game


def folds(first_num, second_num):
    return first_num + second_num, f'{first_num} + {second_num}'


def subtracts(first_num, second_num):
    return first_num - second_num, f'{first_num} - {second_num}'


def multiplies(first_num, second_num):
    return first_num * second_num, f'{first_num} * {second_num}'


def build_logic():
    '''Game logic brain-calc'''

    first_num = make_num(START_OF_RANGE, END_OF_RANGE)
    second_num = make_num(START_OF_RANGE, END_OF_RANGE)
    index_operator = make_num(PLUS, MINUS)

    if index_operator == PLUS:
        correct_answer, task = folds(first_num, second_num)
    elif index_operator == MINUS:
        correct_answer, task = subtracts(first_num, second_num)
    else:
        correct_answer, task = multiplies(first_num, second_num)

    return str(correct_answer), task


def starts_the_game():
    build_game(build_logic, BRAIN_CALC)
