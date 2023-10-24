from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_EVEN, \
    START_OF_RANGE, END_OF_RANGE
from brain_games.core import start_game


def is_even(random_number):
    return random_number % 2 == 0


def get_answer_task():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = make_num(START_OF_RANGE, END_OF_RANGE)
    task = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'

    return correct_answer, task


def start_even():
    start_game(get_answer_task, QUESTION_BRAIN_EVEN)
