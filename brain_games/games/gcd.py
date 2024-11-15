from collections.abc import Sequence
from random import randint

from brain_games.games.main import play_game

GCD_RULES = 'Find the greatest common divisor of given numbers.'


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_question_generator() -> Sequence[Sequence[str], str]:
    question = randint(1, 10), randint(1, 10)
    answer = str(gcd(*question))
    question = ' '.join(map(str, question))
    return question, answer


def main() -> None:
    play_game(rules=GCD_RULES, question_generator=gcd_question_generator)
