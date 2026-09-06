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
    instructions="""You are a data analyst. Use python to calculate precisely.""",
    input="What is the compound interest on a principal of $10,000 at an annual interest rate of 5% compounded monthly for 10 years?",
    tools=[{"type": "code_interpreter", "container": {"type": "auto" }}] 
)

# inspect what happened under the hood.
for item in response.output:
    if item.type == "code_interpreter_call":
        print("Python code the model wrote:")
        print(item.code)
        print("Python code output:")
        print(item.outputs)
    elif item.type == "message":
        print("Model's final answer:")
        print(response.output_text)


