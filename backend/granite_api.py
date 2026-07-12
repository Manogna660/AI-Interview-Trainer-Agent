import os
from dotenv import load_dotenv

load_dotenv()

# Dummy mode (works without IBM credentials)
USE_DUMMY = True

if not USE_DUMMY:
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference

    credentials = Credentials(
        url=os.getenv("IBM_URL"),
        api_key=os.getenv("IBM_API_KEY")
    )

    model = ModelInference(
        model_id="ibm/granite-3-3-8b-instruct",
        credentials=credentials,
        project_id=os.getenv("IBM_PROJECT_ID")
    )

def generate_interview(role):

    if USE_DUMMY:

        return f"""
# AI Interview Questions

## HR Questions

1. Tell me about yourself.

2. Why do you want to work as a {role}?

3. Explain a challenging project you completed.

## Technical Questions

1. Explain Machine Learning.

2. Difference between Supervised and Unsupervised Learning.

3. Explain Cross Validation.

4. What is Overfitting?

5. Explain Feature Engineering.

## Coding Question

Write a Python program to reverse a string.

"""

    prompt = f"""
Generate interview questions for {role}.

Include

3 HR

5 Technical

1 Coding
"""

    response = model.generate_text(
        prompt=prompt,
        params={
            "temperature":0.5,
            "max_new_tokens":400
        }
    )

    return response