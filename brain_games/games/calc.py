from collections.abc import Sequence
from random import randint

CALC_RULE = 'What is the result of the expression?'


def calc_question_generator() -> Sequence[str, str]:
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operator = ['+', '-', '*'][randint(0, 2)]
    question = f'{num1} {operator} {num2}'
    answer = 0
    match operator:
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case '*':
            answer = num1 * num2
    return question, str(answer)
