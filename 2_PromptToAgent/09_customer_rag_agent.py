import os
from pathlib import Path
from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
if not PROJECT_ENDPOINT:
    raise RuntimeError(
        "AZURE_AI_PROJECT_ENDPOINT is missing from the repository .env file. "
        "Copy the project endpoint from the Azure AI Foundry project Overview page."
    )

DEPLOYMENT_NAME = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME")
if not DEPLOYMENT_NAME:
    raise RuntimeError(
        "AZURE_AI_MODEL_DEPLOYMENT_NAME is missing from the repository .env file. "
        "Set it to the exact deployment name in Azure AI Foundry."
    )

AGENT_NAME = os.environ.get("AZURE_AI_AGENT_NAME", "cloudxeus-support-rag-agent")

SYSTEM_PROMPT = """
You are a customer support assistant for CloudXeus Technology Services.

Answer the customer's question using ONLY the provided sources.

After your answer, cite the source URL you used.

If the sources do not contain the answer, say:
"I don't have that information in the available knowledge base."

Then suggest contacting support@cloudxeus.com.

Never invent policies, prices, refund rules, or timelines.
"""

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=AzureCliCredential()
)

agent = project.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=SYSTEM_PROMPT,
    ),
)