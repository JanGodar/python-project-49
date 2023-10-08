from brain_games.random_num import make_num
from brain_games.constant import EVEN


def build_logic():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = make_num()
    task = f'{random_number}'
    correct_answer = 'yes' if random_number % EVEN == 0 else 'no'

    return correct_answer, task
