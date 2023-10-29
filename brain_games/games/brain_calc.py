from brain_games.utils import get_num
from brain_games.constant import QUESTION_CALC_GAME, OPERATORS
from brain_games.core import start_game


def get_operator():
    index_operator = get_num(0, 2)
    return OPERATORS[index_operator]


def get_answer(first_num, second_num, operator):
    match operator:
        case '+':
            correct_answer = first_num + second_num
        case '-':
            correct_answer = first_num - second_num
        case '*':
            correct_answer = first_num * second_num
    return correct_answer


def get_answer_and_task():
    first_num = get_num()
    second_num = get_num()

    operator = get_operator()
    correct_answer = get_answer(first_num, second_num, operator)
    task = f'{first_num} {operator} {second_num}'

    return str(correct_answer), task


def start_calc_game():
    start_game(get_answer_and_task, QUESTION_CALC_GAME)
