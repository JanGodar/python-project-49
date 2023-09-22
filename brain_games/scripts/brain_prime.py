#!/usr/bin/env python3
from brain_games.games.brain_prime_logic import game_quest, log_prime
from brain_games.games.game import engine_game

def main():
    '''Script for calling the game brain-prime'''
    engine_game(log_prime, game_quest)

if __name__ == "__main__":
    main()
