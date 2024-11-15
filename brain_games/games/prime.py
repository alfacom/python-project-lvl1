from collections.abc import Sequence
from random import randint

from brain_games.games.main import play_game, YES, NO

PRIME_RULE = f'Answer "{YES}" if given number is prime. Otherwise answer "{NO}".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_question_generator() -> Sequence[int, str]:
    question = randint(1, 100)
    answer = YES if is_prime(question) else NO
    return question, answer


def main() -> None:
    play_game(rules=PRIME_RULE, question_generator=prime_question_generator)
