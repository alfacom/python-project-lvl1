#!/usr/bin/env python3
from brain_games.games.calc import CALC_RULE, calc_question_generator
from brain_games.games.main import play_game


def main():
    play_game(rules=CALC_RULE, question_generator=calc_question_generator)


if __name__ == '__main__':
    main()
