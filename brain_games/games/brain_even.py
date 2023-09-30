from brain_games.random_num import make_num
from brain_games.constant import EVEN


def ask():
    '''Returns the task that the player
       needs to complete'''

    return 'Answer "yes" if the number is even, otherwise answer "no".'


def build_logic():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = make_num()
    task = f'{random_number}'
    correct_answer = 'yes' if random_number % EVEN == 0 else 'no'

    return correct_answer, task
