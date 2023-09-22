import random
from math import sqrt

def game_quest():
    '''Brain-prime game question'''

    return ('Answer "yes" if given number is prime. Otherwise answer "no".')


def log_prime():
    '''Game logic brain-prime'''

    random_num = random.randint(1, 100)
    task = random_num

    correct_answer = 'yes'
    for i in range(2, random_num // 2 + 1):
        if random_num % i == 0:
            correct_answer = 'no'
    if random_num == 1:
        correct_answer = 'no'

    return correct_answer, task
