#!/usr/bin/env python3
import random
import prompt


def main():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number even, otherwise anser "no".')
    counter = 0

    while counter != 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer not in ['yes', 'no']:
            print(f'"{user_answer}" is wrong answer')

        elif random_number % 2 == 0:
            if user_answer == 'yes':
                print('Correct!')
                counter += 1
            elif user_answer == 'no':
                print(f'"{user_answer}" is wrong answer ;(.'
                      f'Correct answer was "yes".')

        elif random_number % 2 != 0:
            if user_answer == 'yes':
                print(f'"{user_answer}" is wrong answer ;(.'
                      f'Correct answer was "no"')
            elif user_answer == 'no':
                print('Correct!')
                counter += 1

    print(f'Congradulations, {name}!')


if __name__ == "__main__":
    main()
