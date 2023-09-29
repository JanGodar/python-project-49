#!/usr/bin/env python3
from brain_games.games.brain_prog import ask, build_log
from brain_games.game import engine_game


def main():
    '''Script for callig the game brain-progression'''
    engine_game(build_log, ask)


if __name__ == "__main__":
    main()
