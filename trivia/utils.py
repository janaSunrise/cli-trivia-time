import typing as t
from random import shuffle

import colorama
import html2text
import inquirer

colorama.init(autoreset=True)
handler = html2text.HTML2Text()
handler.ignore_links = True


def to_text(text: str) -> t.Union[str, list]:
    if isinstance(text, list):
        return [handler.handle(elem).strip().replace("\n", " ") for elem in text]

    return handler.handle(text).strip().replace("\n", " ")


def get_color(color: str) -> str:
    return getattr(colorama.Fore, color.upper())


def get_bright_color(color: str) -> str:
    return getattr(colorama.Style, "BRIGHT") + get_color(color)


def get_clean_question_type(question_type: str) -> str:
    if question_type == "true and false":
        return "boolean"
    else:
        return "multiple"


def evaluate_score(json: dict, answers: dict) -> int:
    score = 0
    correct_answers = []

    for i, result in enumerate(json):
        correct_answers.append(result["correct_answer"])

    for i in range(len(correct_answers)):
        if str(answers[str(i + 1)]) == correct_answers[i]:
            score += 1

    return score


def generate_quiz_questions(trivia_response: dict, question_type: str) -> list:
    questions = []

    for i, trivia in enumerate(trivia_response):
        question = to_text(trivia["question"])

        choices = to_text(trivia["incorrect_answers"] + [trivia["correct_answer"]])
        shuffle(list(choices))

        if question_type == "multiple":
            questions.append(
                inquirer.List(
                    name=str(i + 1),
                    message=question,
                    choices=choices,
                )
            )
        else:
            questions.append(
                inquirer.Confirm(
                    name=str(i + 1),
                    message=question,
                    default=False
                )
            )

    return questions
