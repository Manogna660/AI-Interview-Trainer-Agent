from backend.granite_api import ask_granite


def recommend(answer):

    prompt = f"""
Based on this interview answer:

{answer}

Suggest

1. Interview tips

2. Skills to improve

3. Online learning resources

4. Final recommendation
"""

    return ask_granite(prompt)