import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output_text}")

