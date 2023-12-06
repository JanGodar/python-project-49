from brain_games.utils import get_num
from brain_games.constant import NUM_PROG_ELEM


def get_list():
    start = get_num()
    step = get_num(1, 10)
    stop = start + step * NUM_PROG_ELEM
    return [i for i in range(start, stop, step)]


def get_question_and_answer():
    miss_index = get_num(0, 9)
    common_list = get_list()
    answer = common_list[miss_index]
    common_list[miss_index] = '..'
    question = ' '.join(map(str, common_list))
    return question, str(answer)
