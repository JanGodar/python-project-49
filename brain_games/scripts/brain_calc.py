#!/usr/bin/env python3
import random
import prompt


def main():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print('What is the result of the expression?')
    counter = 0

    while counter != 3:
        first_random_number = random.randint(1, 100)
        second_random_number = random.randint(1, 100)
        index_operator = random.randint(1, 3)
        if index_operator == 1:
            correct_answer = first_random_number + second_random_number
            print(f'Question: {first_random_number} + {second_random_number}')
        elif index_operator == 2:
            correct_answer = first_random_number - second_random_number
            print(f'Question: {first_random_number} - {second_random_number}')
        else:
            correct_answer = first_random_number * second_random_number
            print(f'Question: {first_random_number} * {second_random_number}')

        user_answer = int(input('Your answer '))

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")

    print(f'Congratulations, {name}!')
