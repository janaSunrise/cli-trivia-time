import inquirer

from .scraper import _get_json
from .utils import evaluate_score, generate_quiz_questions, get_clean_question_type, get_bright_color, get_color

# --- Global Variables ---
question_type = ["True and False", "Multiple Choice"]
question_hard_level = ["any", "easy", "medium", "difficult"]

# --- Question Type section ---
question_type = get_clean_question_type(
    inquirer.list_input(
        message=f"{get_bright_color('YELLOW')}What should be the Trivia Type",
        choices=question_type
    ).lower()
)

# --- Difficulty Section ---
difficulty = inquirer.list_input(
    message=f"{get_bright_color('YELLOW')}What should be the Trivia difficulty?",
    choices=question_hard_level
)

# --- Question Count section ---
question_count = inquirer.text(
    message=f"{get_bright_color('YELLOW')}How many trivia questions to ask?",
    default=10,
)

if not question_count.isnumeric():
    question_count = 5


# -- Get the JSON Response --
trivia_response = _get_json(
    {
        "amount": question_count,
        "difficulty": difficulty,
        "type": question_type
    }
)["results"]


# Start the game!
print(f"{get_bright_color('GREEN')}\nLet's start!\n")

# Initialize the questions, and stuff for starting.
questions = generate_quiz_questions(trivia_response, question_type)

# Ask the questions
answers = inquirer.prompt(questions)

# Evaluate the score and print it.
score = evaluate_score(trivia_response, answers)

color = get_bright_color("RED") if score < (len(trivia_response) / 2) else get_bright_color("GREEN")
print(f"You scored {color}{score} {get_color('RESET')}out of {get_bright_color('LIGHTBLUE_EX')}{len(trivia_response)}.")
