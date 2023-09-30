#!/usr/bin/env python3
from brain_games.games.brain_gcd import ask, build_logic
from brain_games.game import build_game


def main():
    '''Script for calling the game brain-gcd'''
    build_game(build_logic, ask)


if __name__ == "__main__":
    main()
