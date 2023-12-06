from brain_games.utils import get_num


def is_prime(random_num):
    if random_num < 2:
        return False
    for i in range(2, int(random_num ** 0.5 + 1)):
        if random_num % i == 0:
            return False
    return True


def get_question_and_answer():
    random_num = get_num()
    question = random_num
    answer = 'yes' if is_prime(random_num) else 'no'
    return question, answer
