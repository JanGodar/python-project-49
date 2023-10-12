from brain_games.utils import make_num
from brain_games.constant import EVEN, BRAIN_EVEN, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import build_game


def build_logic():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = make_num(START_OF_RANGE, END_OF_RANGE)
    task = f'{random_number}'
    correct_answer = 'yes' if random_number % EVEN == 0 else 'no'

    return correct_answer, task


def starts_the_game():
    build_game(build_logic, BRAIN_EVEN)
