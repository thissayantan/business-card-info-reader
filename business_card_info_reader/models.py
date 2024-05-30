from dotenv import load_dotenv
load_dotenv()  # This loads the environment variables from the .env file

from .prompts import get_business_card_analysis_prompt
from openai import OpenAI
import os

class BaseModel:
    def analyze_image(self, image_url):
        raise NotImplementedError("This method should be overridden by subclasses.")

class OpenAIModel(BaseModel):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No OpenAI API key found in environment variables")
        self.client = OpenAI(api_key=self.api_key)

    def analyze_image(self, image_url):
        prompt = get_business_card_analysis_prompt()
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
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
            max_tokens=1024,
        )
        return response.choices[0].message.content

# Future model classes can be added here following the pattern established by OpenAIModel.
