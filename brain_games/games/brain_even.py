from brain_games.utils import get_num
from brain_games.constant import QUESTION_EVEN_GAME
from brain_games.core import start_game


def is_even(random_number):
    return random_number % 2 == 0


def get_question_and_answer():
    random_number = get_num()
    question = str(random_number)
    answer = 'yes' if is_even(random_number) else 'no'
    return question, answer


def start_even_game():
    start_game(get_question_and_answer, QUESTION_EVEN_GAME)
