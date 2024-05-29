import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

client = OpenAI(api_key=api_key)


def fetch_image_analysis(image_url):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this business card image and extract the information in a structured JSON format.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}


def parse_response(response_content):
    try:
        # Assuming the response_content is a JSON string
        return response_content
    except Exception as e:
        return {"error": "Invalid response format", "details": str(e)}
