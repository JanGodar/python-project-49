#!/usr/bin/env python3
from brain_games.constant import QUESTION_EVEN_GAME
from brain_games.games.brain_even import get_question_and_answer
from brain_games.core import start_game


def main():
    start_game(get_question_and_answer, QUESTION_EVEN_GAME)


if __name__ == "__main__":
    main()
