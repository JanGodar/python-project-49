from brain_games.utils import make_num
from brain_games.constant import CHECK_EVEN, QUESTION_BRAIN_EVEN, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import launches_game


def is_even(random_number):
    return True if random_number % CHECK_EVEN == 0 else False


def build_logic():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = make_num(START_OF_RANGE, END_OF_RANGE)
    task = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'

    return correct_answer, task


def starts_brain_even():
    launches_game(build_logic, QUESTION_BRAIN_EVEN)
