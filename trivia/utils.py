from random import shuffle

import html2text
import inquirer

handler = html2text.HTML2Text()
handler.ignore_links = True


def to_text(text):
    if isinstance(text, list):
        return [handler.handle(elem).strip().replace("\n", " ") for elem in text]

    return handler.handle(text).strip().replace("\n", " ")


def evaluate_score(json, answers):
    score = 0
    correct_answers = []

    for i, result in enumerate(json):
        correct_answers.append(result["correct_answer"])

    for i in range(len(correct_answers)):
        if str(answers[str(i + 1)]) == correct_answers[i]:
            score += 1

    return score


def generate_quiz_questions(trivia_response, question_type):
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
                inquirer.confirm(
                    name=str(i + 1),
                    message=question,
                    default=False
                )
            )

    return questions
