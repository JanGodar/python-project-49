import random

def game_quest():
    '''Returns the brain-progression game question'''

    return 'What number is missing in the progression?'


def log_prog():
    '''logic of the game brain-progression'''

    start = random.randint(1, 100)
    step = random.randint(1, 10)
    miss_index = random.randint(0, 9)
    common_list = [i for i in range(start, start+step*10, step)]
    
    correct_answer = common_list[miss_index]
    common_list[miss_index] = '..'
    
    task = ' '.join(map(str, common_list))
    return str(correct_answer), task
