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
    input="What are the latest development in AI regulations in the European Union?",
    instructions="""You are a helpful assistant always cite your resoures.""",
    tools=[{"type": "web_search"}],   
    tool_choice="auto"
)

print(f"answer: {response.output_text}")

