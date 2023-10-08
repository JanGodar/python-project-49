#!/usr/bin/env python3
from brain_games.games.brain_prog import build_logic
from brain_games.core import build_game
from brain_games.constant import BRAIN_PROG


def main():
    '''Script for callig the game brain-progression'''
    build_game(build_logic, BRAIN_PROG)


if __name__ == "__main__":
    main()
