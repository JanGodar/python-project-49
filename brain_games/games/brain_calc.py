from random import choice
from brain_games.utils import get_num
from brain_games.constant import QUESTION_CALC_GAME, OPERATORS
from brain_games.core import start_game


def get_result_by_math_sign(first_num, second_num, math_sign):
    match math_sign:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def get_question_and_answer():
    first_num, second_num = get_num(), get_num()
    math_sign = choice(OPERATORS)
    question = f'{first_num} {math_sign} {second_num}'
    answer = get_result_by_math_sign(first_num, second_num, math_sign)
    return question, str(answer)


def start_calc_game():
    start_game(get_question_and_answer, QUESTION_CALC_GAME)
