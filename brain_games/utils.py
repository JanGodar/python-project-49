import random
from brain_games.constant import START_RANGE, END_RANGE


def get_num():
    num = random.randint(start = START_RANGE, end = END_RANGE)
    return num
