from collections.abc import Sequence
from random import randint

from brain_games.games.main import play_game, YES, NO

EVEN_RULES = f'Answer "{YES}" if given number is even, otherwise answer "{NO}".'


def even_question_generator() -> Sequence[int, str]:
    question = randint(1, 100)
    answer = YES if question % 2 == 0 else NO
    return question, answer


def main() -> None:
    play_game(rules=EVEN_RULES, question_generator=even_question_generator)