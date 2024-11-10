#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        print(f'Question: {num1} {num2}')
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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()
