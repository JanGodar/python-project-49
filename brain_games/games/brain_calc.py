from brain_games.random_num import make_num
from brain_games.constant import PLUS, MINUS
import random


def ask():
    '''Brain-calc game question'''

    return 'What is the result of the expression?'


def build_logic():
    '''Game logic brain-calc'''

    first_num = make_num()
    second_num = make_num()
    index_operator = random.randint(1, 3)

    if index_operator == PLUS:
        correct_answer = first_num + second_num
        task = f'{first_num} + {second_num}'
    elif index_operator == MINUS:
        correct_answer = first_num - second_num
        task = f'{first_num} - {second_num}'
    else:
        correct_answer = first_num * second_num
        task = f'{first_num} * {second_num}'

    return str(correct_answer), task
