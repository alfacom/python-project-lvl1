#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


def main() -> None:
    name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(3):
        start = randint(1, 10)
        step = randint(1, 10)
        length = randint(5, 10)
        progression = [start + step * i for i in range(length)]
        hidden_index = randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."
        print('Question:', " ".join(map(str, progression)))
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
