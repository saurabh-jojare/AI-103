import os
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

SEARCH_ENDPOINT = os.environ.get("AZURE_SEARCH_ENDPOINT")
INDEX_NAME = os.environ.get("AZURE_SEARCH_INDEX_NAME")

if not SEARCH_ENDPOINT:
    raise RuntimeError("AZURE_SEARCH_ENDPOINT is missing from the repository .env file.")
if not INDEX_NAME:
    raise RuntimeError("AZURE_SEARCH_INDEX_NAME is missing from the repository .env file.")

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=DefaultAzureCredential(),
)

results = search_client.search(
    search_text="refund",
    select=["chunk", "title"],
)

for result in results:
    print(f"Score:  {result['@search.score']:.4f}")
    print(f"Source: {result['title']}")
    print(f"Text:   {result['chunk']}")
    print("---")