#!/usr/bin/env python3
from brain_games.games.main import play_game
from brain_games.games.prime import PRIME_RULE, prime_question_generator


def main():
    play_game(rules=PRIME_RULE, question_generator=prime_question_generator)


if __name__ == '__main__':
    main()
