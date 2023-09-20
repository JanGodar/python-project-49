#!/usr/bin/env python3
from brain_games.games.brain_even_logic import problem_question, logic_random_number
from brain_games.games.game import engine_game


def main():
    '''Even number game script'''
    engine_game(logic_random_number, problem_question)


if __name__ == "__main__":
    main()
