import random
from brain_games.constant import START_RANGE, END_RANGE


def get_num(start=START_RANGE, end=END_RANGE):
    num = random.randint(start, end)
    return num
