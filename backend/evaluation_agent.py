from backend.granite_api import ask_granite


def evaluate_answer(question, answer):

    prompt = f"""
You are an expert interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate it.

Give:

Score out of 10

Strengths

Weaknesses

Improved Answer
"""

    return ask_granite(prompt)