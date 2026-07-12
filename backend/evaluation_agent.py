def evaluate_answer(answer):

    score = 0

    feedback = []

    if len(answer) > 100:
        score += 4
        feedback.append("Detailed answer.")

    if "example" in answer.lower():
        score += 2
        feedback.append("Examples included.")

    if "project" in answer.lower():
        score += 2
        feedback.append("Project experience mentioned.")

    if "team" in answer.lower():
        score += 2
        feedback.append("Teamwork demonstrated.")

    return score, feedback