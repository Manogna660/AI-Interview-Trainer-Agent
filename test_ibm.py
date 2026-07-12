from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from dotenv import load_dotenv
import os

load_dotenv()

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
    prompt="Generate 3 interview questions for a Python Developer.",
    params={
        "max_new_tokens": 100,
        "temperature": 0.5
    }
)

print(response)