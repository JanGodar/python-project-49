from brain_games.utils import get_num


def is_even(random_number):
    return random_number % 2 == 0


def get_question_and_answer():
    random_number = get_num()
    question = str(random_number)
    answer = 'yes' if is_even(random_number) else 'no'
    return question, answer
