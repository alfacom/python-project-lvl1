import prompt

from brain_games.cli import welcome_user

ROUNDS = 3


def play_game(rules: str, question_generator: callable,
              num_rounds: int = ROUNDS) -> None:
    name = welcome_user()
    print(rules)
    for _ in range(num_rounds):
        question, correct_answer = question_generator()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
