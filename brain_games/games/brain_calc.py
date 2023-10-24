from brain_games.utils import make_num
from brain_games.constant import CALC_PLUS, CALC_MINUS, START_OF_RANGE, \
    END_OF_RANGE, QUESTION_BRAIN_CALC
from brain_games.core import start_game


def consider_answer_task(first_num, second_num):
    index_operator = make_num(CALC_PLUS, CALC_MINUS)
    if index_operator == CALC_PLUS:
        correct_answer = first_num + second_num
        task = f'{first_num} + {second_num}'
    elif index_operator == CALC_MINUS:
        correct_answer = first_num - second_num
        task = f'{first_num} - {second_num}'
    else:
        correct_answer = first_num * second_num
        task = f'{first_num} * {second_num}'
    return correct_answer, task


def get_answer_task():
    '''Game logic brain-calc'''

    first_num = make_num(START_OF_RANGE, END_OF_RANGE)
    second_num = make_num(START_OF_RANGE, END_OF_RANGE)

    correct_answer, task = consider_answer_task(first_num, second_num)

    return str(correct_answer), task


def start_calc():
    start_game(get_answer_task, QUESTION_BRAIN_CALC)
