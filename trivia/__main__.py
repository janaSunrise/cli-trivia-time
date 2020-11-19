import inquirer

from .scraper import _get_json
from .utils import evaluate_score, to_text, generate_quiz_questions

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
print("\nLet's start!\n")

# Initialize the questions, and stuff for starting.
questions = generate_quiz_questions(trivia_response)

# Ask the questions
answers = inquirer.prompt(questions)

# Evaluate the score and print it.
score = evaluate_score(trivia_response, answers)

print(f"You scored {score} out of {len(trivia_response)}.")
