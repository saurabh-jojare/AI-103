import os
from pathlib import Path
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, FunctionTool
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
if not PROJECT_ENDPOINT:
    raise RuntimeError(
        "AZURE_AI_PROJECT_ENDPOINT is missing from the repository .env file. "
        "Copy the project endpoint from the Azure AI Foundry project Overview page."
    )
    
AGENT_NAME="IT-HelpDesk-Agent"
DEPLOYMENT_NAME = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME")
if not DEPLOYMENT_NAME:
    raise RuntimeError(
        "AZURE_AI_MODEL_DEPLOYMENT_NAME is missing from .env. "
        "Set it to the exact deployment name shown in Azure AI Foundry."
    )

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

tools = [
    FunctionTool(
        name="get_password_reset_steps",
        description="Get the company password reset steps.",
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        strict=True,
    ),
    FunctionTool(
        name="get_vpn_troubleshooting_steps",
        description="Get troubleshooting steps for VPN connection issues.",
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        strict=True,
    ),
    FunctionTool(
        name="get_software_install_guide",
        description="Get installation instructions for a supported software package.",
        parameters={
            "type": "object",
            "properties": {
                "software_name": {
                    "type": "string",
                    "description": "The software name, for example Slack, Zoom, or VS Code."
                }
            },
            "required": ["software_name"],
            "additionalProperties": False,
        },
        strict=True,
    ),
]

agent=client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=(
            "You are an IT support assistant for a company. "
            "Help users with password resets, VPN issues, and software installation. "
            "Give clear, step-by-step answers. "
            "If the question is outside IT support topics, politely say so."
        ),
        tools=tools
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")