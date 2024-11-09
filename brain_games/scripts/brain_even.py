#!/usr/bin/env python3
from random import random

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = int(random() * 100)
        is_even = random_number % 2 == 0
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if is_even and answer == 'yes' or not is_even and answer == 'no':
            print('Correct!')
        elif (answer not in ['yes', 'no']
              or is_even and answer == 'no'
              or not is_even and answer == 'yes'):
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
