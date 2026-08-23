import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")

endpoint = "https://foundry-openai-delete.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4"
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

problem = """A distributed system is experiencing intermittent failures in its microservices architecture. 
The failures are causing delays in processing requests and impacting the overall performance of the system. 
The team suspects that the issue may be related to network latency, resource contention, or misconfigured service dependencies. 
They need to identify the root cause of the failures and implement a solution to improve the reliability and performance of the system.
"""

response = client.responses.create(
    model=deployment_name,
    input=problem,
    instructions="You are a Senior Software Archittect.", 
    reasoning={"effort": "high"}
)

print(f"answer: {response.output_text}")

