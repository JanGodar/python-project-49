#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0

    while counter != 3:
        random_number = random.randint(1, 100)
        flag = True
        print(f'Question: {random_number}')

        for i in range(2, random_number//2 + 1):
            if random_number % i == 0:
                flag = False

        user_answer = prompt.string('Your answer: ')
        if flag:
            if user_answer == 'yes':
                print('Correct!')
                counter += 1
            else:
                print(f'{user_answer} is wrong answer')
        else:
            if user_answer == 'yes':
                print(f'{user_answer} is wrong answer')
            else:
                print('Correct')
                counter += 1

    print(f'Congradulations, {name}!')


if __name__ == "__main__":
    main()
