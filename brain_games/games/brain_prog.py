from brain_games.random_num import make_num
from brain_games.constant import NUM_OF_PROGRESSION_ELEM
import random


def build_logic():
    '''logic of the game brain-progression'''

    start = make_num()
    step = random.randint(1, 10)
    miss_index = random.randint(0, 9)
    stop = start + step * NUM_OF_PROGRESSION_ELEM
    common_list = [i for i in range(start, stop, step)]

    correct_answer = common_list[miss_index]
    common_list[miss_index] = '..'

    task = ' '.join(map(str, common_list))
    return str(correct_answer), task
