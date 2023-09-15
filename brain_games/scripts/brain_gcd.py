#!/usr/bin/env python3
import random
import prompt

def main():
    #Приветствие
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print('Find the greatest common divisor of given numbers.')
    counter = 0

    while counter != 3:
        first_random_number = random.randint(1, 100)
        second_random_number = random.randint(1, 100)
        print(f'Question: {first_random_number} {second_random_number}')
        user_answer = prompt.integer('Your answer: ')

        if first_random_number == second_random_number:
            gsd = first_random_number
        else:
            max_number = max(first_random_number, second_random_number)
            min_number = min(first_random_number, second_random_number)
            flag = True
            while flag:
                if max_number % min_number != 0:
                    max_number, min_number = min_number, max_number % min_number
                else:
                    gsd = min_number
                    flag = False

        if gsd == user_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {gsd}.\nLet is try again, {name}')



    print(f'Congradulations, {name}!')

if __name__ == "__main__":
    main()
