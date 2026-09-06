import base64
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

image_path = Path(__file__).resolve().parent.parent / "image022.png"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

#print("image_data: ", image_data)
response = client.responses.create(
    model=deployment_name,
    instructions="You are helpful assistance that reads and extract text from images.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text", 
                    "text": "Extract all the text from the image and provide a summary of the content."
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{image_data}"
                },
            ],
        }
    ],
)

print(f"answer: {response.output_text}")

