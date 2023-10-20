from brain_games.utils import make_num
from brain_games.constant import QUESTION_BRAIN_PROG, NUM_OF_PROG_ELEM, \
                                 START_OF_RANGE, END_OF_RANGE
from brain_games.core import launches_game


def gives_list():
    start = make_num(START_OF_RANGE, END_OF_RANGE)
    step = make_num(1, 10)
    stop = start + step * NUM_OF_PROG_ELEM
    return [i for i in range(start, stop, step)]


def build_logic():
    '''logic of the game brain-progression'''

    miss_index = make_num(0, 9)
    common_list = gives_list()
    correct_answer = common_list[miss_index]

    common_list[miss_index] = '..'
    task = ' '.join(map(str, common_list))

    return str(correct_answer), task


def starts_brain_prog():
    launches_game(build_logic, QUESTION_BRAIN_PROG)
