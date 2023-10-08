#!/usr/bin/env python3
from brain_games.games.brain_even import build_logic
from brain_games.core import build_game
from brain_games.constant import BRAIN_EVEN


def main():
    '''Even number game script'''
    build_game(build_logic, BRAIN_EVEN)


if __name__ == "__main__":
    main()
