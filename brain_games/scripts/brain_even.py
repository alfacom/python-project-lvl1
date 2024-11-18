#!/usr/bin/env python3
from brain_games.games.even import EVEN_RULE, even_question_generator
from brain_games.games.main import play_game


def main():
    play_game(rules=EVEN_RULE, question_generator=even_question_generator)


if __name__ == '__main__':
    main()
