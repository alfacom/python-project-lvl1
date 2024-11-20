from collections.abc import Sequence
from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def question_generator() -> Sequence[Sequence[str], str]:
    question = randint(1, 10), randint(1, 10)
    answer = str(gcd(*question))
    question = ' '.join(map(str, question))
    return question, answer
