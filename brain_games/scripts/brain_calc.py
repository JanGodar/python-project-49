#!/usr/bin/env python3
from brain_games.games.brain_calc import build_logic
from brain_games.core import build_game
from brain_games.constant import BRAIN_CALC


def main():
    '''Script for calling the game brain-calc'''
    build_game(build_logic, BRAIN_CALC)


if __name__ == '__main__':
    main()
