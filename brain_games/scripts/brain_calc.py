#!/usr/bin/env python3
from brain_games.games.brain_calc_logic import game_quest, log_calc
from brain_games.games.game import engine_game

def main():
    '''Game scripts solution expression'''
    engine_game(log_calc, game_quest)

if __name__ == '__main__':
    main()
