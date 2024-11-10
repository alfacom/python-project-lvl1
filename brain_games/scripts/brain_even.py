#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 100)
        correct_answer = "yes" if random_number % 2 == 0 else "no"
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
