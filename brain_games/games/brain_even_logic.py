import random

def problem_question():
    '''Returns the task that the player
       needs to complete'''

    return 'Answer "yes" if the number is  even, otherwise answer "no".'


def logic_random_number():
    '''Game logic that checks whether a number
       is prime or not'''

    random_number = random.randint(1, 100)
    task = f'{random_number}'
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'

    return correct_answer, task

