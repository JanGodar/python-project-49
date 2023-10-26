from brain_games.utils import get_num
from brain_games.constant import QUESTION_PROG_GAME, NUM_PROG_ELEM, \
    START_RANGE, END_RANGE
from brain_games.core import start_game


def get_list():
    start = get_num(START_RANGE, END_RANGE)
    step = get_num(1, 10)
    stop = start + step * NUM_PROG_ELEM
    return [i for i in range(start, stop, step)]


def get_answer_task():
    '''logic of the game brain-progression'''

    miss_index = get_num(0, 9)
    common_list = get_list()
    correct_answer = common_list[miss_index]

    common_list[miss_index] = '..'
    task = ' '.join(map(str, common_list))

    return str(correct_answer), task


def start_prog_game():
    start_game(get_answer_task, QUESTION_PROG_GAME)
