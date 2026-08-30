import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, WebSearchTool
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
if not PROJECT_ENDPOINT:
    raise RuntimeError(
        "AZURE_AI_PROJECT_ENDPOINT is missing from the repository .env file. "
        "Copy the project endpoint from the Azure AI Foundry project Overview page."
    )

AGENT_NAME = "web-search-lab-agent"
DEPLOYMENT_NAME = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME")
if not DEPLOYMENT_NAME:
    raise RuntimeError(
        "AZURE_AI_MODEL_DEPLOYMENT_NAME is missing from .env. "
        "Set it to the exact deployment name shown in Azure AI Foundry."
    )

client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

agent=client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=
            "You are a helpful assistant. Use web search to answer questions that require current information."
        ,tools=[WebSearchTool()]
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")