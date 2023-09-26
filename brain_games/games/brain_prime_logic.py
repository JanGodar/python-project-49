import random


def ask():
    '''Brain-prime game question'''

    return ('Answer "yes" if given number is prime. Otherwise answer "no".')


def build_log():
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
