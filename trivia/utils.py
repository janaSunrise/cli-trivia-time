import html2text

handler = html2text.HTML2Text()
handler.ignore_links = True

def to_text(text):
    if isinstance(text, list):
        return [handler.handle(elem).strip() for elem in text]

    return handler.handle(text).strip()

def evaluate_score(json, answers):
    score = 0
    correct_answers = []

    for i, result in enumerate(json):
        correct_answers.append(result["correct_answer"])

    for i in range(len(correct_answers)):
        if answers[str(i + 1)] == correct_answers[i]:
            score += 1

    return score
