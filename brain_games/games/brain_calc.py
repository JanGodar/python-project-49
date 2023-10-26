from brain_games.utils import get_num
from brain_games.constant import START_RANGE, END_RANGE, \
    QUESTION_CALC_GAME
from brain_games.core import start_game


def get_operator_answer(first_num, second_num):
    list_operators = ['+', '-', '*']
    index_operator = get_num(0, 2)
    operator = list_operators[index_operator]

    match index_operator:
        case 0:
            correct_answer = first_num + second_num
        case 1:
            correct_answer = first_num - second_num
        case 2:
            correct_answer = first_num * second_num
    return operator, correct_answer


def get_answer_task():
    '''Game logic brain-calc'''

    first_num = get_num(START_RANGE, END_RANGE)
    second_num = get_num(START_RANGE, END_RANGE)

    operator, correct_answer = get_operator_answer(first_num, second_num)
    task = f'{first_num} {operator} {second_num}'

    return str(correct_answer), task


def start_calc_game():
    start_game(get_answer_task, QUESTION_CALC_GAME)
