import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()


def ask_granite(prompt):

    credentials = Credentials(
        url=os.getenv("IBM_URL"),
        api_key=os.getenv("IBM_API_KEY")
    )

    model = ModelInference(
        model_id="ibm/granite-4-h-small",
        credentials=credentials,
        project_id=os.getenv("IBM_PROJECT_ID")
    )

    response = model.generate_text(
        prompt=prompt,
        params={
            "max_new_tokens":300,
            "temperature":0.5
        }
    )

    return response


def generate_interview(job_role, experience):

    prompt = f"""
You are an AI Interview Trainer Agent.

Candidate Details:
Job Role: {job_role}
Experience Level: {experience}

Generate:
1. 10 Technical Interview Questions
2. 5 HR Interview Questions
3. Model Answers
4. Interview Preparation Tips
5. Common Mistakes

Tailor the questions according to the job role and experience level.
"""

    return ask_granite(prompt)