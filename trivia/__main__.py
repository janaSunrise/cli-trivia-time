import inquirer

from .scraper import _get_json
from .utils import get_text

# Start the game!
print("Let's start!\n")

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

trivia = _get_json({
    "amount": question_count,
    "difficulty": difficulty,
    "type": "multiple"
})

print(trivia["results"][0])
