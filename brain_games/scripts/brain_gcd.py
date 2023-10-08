#!/usr/bin/env python3
from brain_games.games.brain_gcd import build_logic
from brain_games.core import build_game
from brain_games.constant import BRAIN_GCD


def main():
    '''Script for calling the game brain-gcd'''
    build_game(build_logic, BRAIN_GCD)


if __name__ == "__main__":
    main()
