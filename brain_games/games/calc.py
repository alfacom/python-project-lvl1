from collections.abc import Sequence
from random import randint

from brain_games.games.main import play_game

CALC_RULE = 'What is the result of the expression?'


def calc_question_generator() -> Sequence[str, str]:
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operator = ['+', '-', '*'][randint(0, 2)]
    question = f'{num1} {operator} {num2}'
    answer = eval(question)
    return question, str(answer)


def main() -> None:
    play_game(rules=CALC_RULE, question_generator=calc_question_generator)
