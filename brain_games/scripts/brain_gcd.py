#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print('Find the greatest common divisor of given numbers.')
    counter = 0

    while counter != 3:
        first_random_num = random.randint(1, 100)
        second_random_num = random.randint(1, 100)
        print(f'Question: {first_random_num} {second_random_num}')
        user_answer = prompt.integer('Your answer: ')

        if first_random_num == second_random_num:
            gsd = first_random_num
        else:
            max_num = max(first_random_num, second_random_num)
            min_num = min(first_random_num, second_random_num)
            flag = True
            while flag:
                if max_num % min_num != 0:
                    max_num, min_num = min_num, max_num % min_num
                else:
                    gsd = min_num
                    flag = False

        if gsd == user_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {gsd}.\n'
                  f'Let is try again, {name}')
    print(f'Congradulations, {name}!')


if __name__ == "__main__":
    main()
