import random
import operator
from brain_games.utils import get_num
from brain_games.constant import OPERATORS


def get_math_sign(math_sign):
    match math_sign:
        case '+':
            return operator.add
        case '-':
            return operator.sub
        case '*':
            return operator.mul


def get_question_and_answer():
    first_rand_num, second_rand_num = get_num(), get_num()
    math_sign = random.choice(OPERATORS)
    question = f'{first_rand_num} {math_sign} {second_rand_num}'
    get_result = get_math_sign(math_sign)
    answer = get_result(first_rand_num, second_rand_num)
    return question, str(answer)
