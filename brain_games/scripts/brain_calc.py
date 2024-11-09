#!/usr/bin/env python3
from random import random

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        num1 = int(random() * 100)
        num2 = int(random() * 100)
        operator = ['+', '-', '*'][int(random() * 3)]
        question = f'{num1} {operator} {num2}'
        correct_answer = str(eval(question))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
