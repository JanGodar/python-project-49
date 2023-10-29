from brain_games.utils import get_num
from brain_games.constant import QUESTION_EVEN_GAME
from brain_games.core import start_game


def is_even(random_number):
    return random_number % 2 == 0


def get_answer_and_task():
    random_number = get_num()
    task = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'

    return correct_answer, task


def start_even_game():
    start_game(get_answer_and_task, QUESTION_EVEN_GAME)
