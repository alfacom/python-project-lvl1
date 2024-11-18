#!/usr/bin/env python3
from brain_games.games.main import play_game
from brain_games.games.progression import PROGRESSION_RULE, \
    progression_question_generator


def main():
    play_game(rules=PROGRESSION_RULE,
              question_generator=progression_question_generator)


if __name__ == '__main__':
    main()
