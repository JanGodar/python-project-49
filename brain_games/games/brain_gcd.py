from brain_games.utils import get_num
from brain_games.constant import QUESTION_GCD_GAME
from brain_games.core import start_game
import math


def get_answer(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_answer_and_task():
    first_num = get_num()
    second_num = get_num()

    task = f'{first_num} {second_num}'
    correct_answer = get_answer(first_num, second_num)

    return str(correct_answer), task


def start_gcd_game():
    start_game(get_answer_and_task, QUESTION_GCD_GAME)
