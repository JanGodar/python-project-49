from brain_games.utils import get_num
import math


def get_answer(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_question_and_answer():
    first_num, second_num = get_num(), get_num()
    question = f'{first_num} {second_num}'
    answer = get_answer(first_num, second_num)
    return question, str(answer)
