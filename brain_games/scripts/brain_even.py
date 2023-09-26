#!/usr/bin/env python3
from brain_games.games.brain_even_logic import ask, build_log
from brain_games.games.game import engine_game


def main():
    '''Even number game script'''
    engine_game(build_log, ask)


if __name__ == "__main__":
    main()
