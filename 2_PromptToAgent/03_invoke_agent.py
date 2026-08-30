import os
from pathlib import Path
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
if not PROJECT_ENDPOINT:
    raise RuntimeError(
        "AZURE_AI_PROJECT_ENDPOINT is missing from the repository .env file. "
        "Copy the project endpoint from the Azure AI Foundry project Overview page."
    )

AGENT_NAME="IT-HelpDesk-Agent"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai=client.get_openai_client()

response=openai.responses.create(
    extra_body={"agent_reference":{"name":AGENT_NAME,"type":"agent_reference"}},
    input="How do I reset my company password?"
)

print(response.output_text)