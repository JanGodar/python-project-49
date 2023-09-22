#!/usr/bin/env python3
from brain_games.games.brain_even_logic import game_quest, log_even
from brain_games.games.game import engine_game


def main():
    '''Even number game script'''
    engine_game(log_even, game_quest)


if __name__ == "__main__":
    main()
