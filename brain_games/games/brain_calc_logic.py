import random


def game_quest():
    '''Brain-calc game question'''

    return 'What is the result of the expression?'


def log_calc():
    '''Game logic brain-calc'''

    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    index_operator = random.randint(1, 3)

    if index_operator == 1:
        correct_answer = first_num + second_num
        task = f'{first_num} + {second_num}'
    elif index_operator == 2:
        correct_answer = first_num - second_num
        task = f'{first_num} - {second_num}'
    else:
        correct_answer = first_num * second_num
        task = f'{first_num} * {second_num}'

    return str(correct_answer), task
