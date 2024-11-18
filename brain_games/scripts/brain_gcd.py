#!/usr/bin/env python3
from brain_games.games.gcd import GCD_RULE, gcd_question_generator
from brain_games.games.main import play_game


def main():
    play_game(rules=GCD_RULE, question_generator=gcd_question_generator)


if __name__ == '__main__':
    main()
