import inquirer

from .scraper import _get_json
from .utils import evaluate_score, to_text

from random import shuffle

# Ask for the input
difficulty = inquirer.list_input(
    message="What should be the Trivia difficulty?",
    choices=["any", "easy", "medium", "difficult"]
)

question_count = inquirer.text(
    message="How many trivia questions to ask?",
    default=10,
)

# Do validation for the question count
if not question_count.isnumeric():
    question_count = 10


# Get the JSON Response
trivia_response = _get_json(
    {
        "amount": question_count,
        "difficulty": difficulty,
        "type": "multiple"
    }
)["results"]


# Start the game!
print("Let's start!\n")

# Initialize the questions, and stuff for starting.
questions = []

for i, trivia in enumerate(trivia_response):
    question = to_text(trivia_response[i]["question"])

    choices = to_text(trivia_response[i]["incorrect_answers"] + [trivia_response[i]["correct_answer"]])
    shuffle(choices)
    print(i)

    questions.append(
        inquirer.List(
            name=str(i + 1),
            message=question,
            choices=choices,
        )
    )

# Ask the questions
answers = inquirer.prompt(questions)


# Evaluate the score and print it.
score = evaluate_score(trivia_response, answers)

print(f"You scored {score} out of {len(trivia_response)}.")
