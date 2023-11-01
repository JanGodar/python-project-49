from brain_games.utils import get_num
from brain_games.constant import QUESTION_GCD_GAME
from brain_games.core import start_game
import math


def get_answer(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_question_and_answer():
    first_num, second_num = get_num(), get_num()
    question = f'{first_num} {second_num}'
    answer = get_answer(first_num, second_num)
    return question, str(answer)


def start_gcd_game():
    start_game(get_question_and_answer, QUESTION_GCD_GAME)
