#!/usr/bin/env python3
from brain_games.games.brain_prime import build_logic
from brain_games.core import build_game
from brain_games.constant import BRAIN_PRIME


def main():
    '''Script for calling the game brain-prime'''
    build_game(build_logic, BRAIN_PRIME)


if __name__ == "__main__":
    main()
