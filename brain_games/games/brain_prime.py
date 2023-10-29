from brain_games.utils import get_num
from brain_games.constant import QUESTION_PRIME_GAME
from brain_games.core import start_game


def is_prime(random_num):
    if random_num < 2:
        return False
    for i in range(2, int(random_num ** 0.5 + 1)):
        if random_num % i == 0:
            return False
    return True


def get_answer_and_task():
    random_num = get_num()
    task = random_num
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    return correct_answer, task


def start_prime_game():
    start_game(get_answer_and_task, QUESTION_PRIME_GAME)
