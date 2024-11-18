from collections.abc import Sequence
from random import randint

PRIME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_question_generator() -> Sequence[int, str]:
    question = randint(1, 100)
    answer = "yes" if is_prime(question) else "no"
    return question, answer
