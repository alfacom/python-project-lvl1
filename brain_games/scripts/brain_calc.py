#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        operator = ['+', '-', '*'][randint(0, 2)]
        question = f'{num1} {operator} {num2}'
        correct_answer = eval(question)
        print(f'Question: {question}')
        answer = prompt.integer('Your answer: ')
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
