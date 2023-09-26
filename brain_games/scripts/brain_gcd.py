#!/usr/bin/env python3
from brain_games.games.brain_gcd_logic import ask, build_log
from brain_games.games.game import engine_game


def main():
    '''Script for calling the game brain-gcd'''
    engine_game(build_log, ask)


if __name__ == "__main__":
    main()
