#!/usr/bin/env python3
from random import random

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = int(random() * 100)
        num2 = int(random() * 100)
        print(f'Question: {num1} {num2}')
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        correct_answer = gcd(num1, num2)
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
