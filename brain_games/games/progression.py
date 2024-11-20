from collections.abc import Sequence
from random import randint

RULE = 'What number is missing in the progression?'


def question_generator() -> Sequence[str]:
    start = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = [start + step * i for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return " ".join(map(str, progression)), str(correct_answer)
