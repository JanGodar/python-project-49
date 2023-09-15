#!/usr/bin/env python3
import random
import prompt

def main():
    #Приветствие
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


    print('What number is missing in the progression?')
    counter = 0

    while counter != 3:
        random_number = random.randint(1, 100)
        step = random.randint(1, 10)
        missing_index = random.randint(0, 9)
        common_list = [i for i in range(random_number, random_number+step*10, step)]
        lost_number = common_list[missing_index]
        common_list[missing_index] = '..'

        print(f'Question: {common_list}')
        user_answer = prompt.integer('Your answer: ')

        if user_answer == lost_number:
            print('Correct!')
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {lost_number}.\nLet's try again, {name}!")

    print(f'Congradulations, {name}!')

if __name__ == "__main__":
    main()

