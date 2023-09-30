#!/usr/bin/env python3
from brain_games.games.brain_prime import ask, build_logic
from brain_games.game import build_game


def main():
    '''Script for calling the game brain-prime'''
    build_game(build_logic, ask)


if __name__ == "__main__":
    main()
