from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO

load_dotenv()  # This loads the environment variables from the .env file

from .prompts import get_business_card_analysis_prompt


class BaseModel:
    def analyze_image(self, image_url):
        raise NotImplementedError("This method should be overridden by subclasses.")


class OpenAIModel(BaseModel):
    def __init__(self):
        from openai import OpenAI

        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No OpenAI API key found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
        print("OpenAI Model initialized")

    def analyze_image(self, image_url):
        prompt = get_business_card_analysis_prompt()
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt},
                {
                    "role": "system",
                    "content": {
                        "type": "image_url",
                        "image_url": image_url,
                    },
                },
            ],
            max_tokens=1024,
        )
        return response.choices[0].message.content


class GoogleGeminiModel(BaseModel):
    def __init__(self):
        import google.generativeai as genai

        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("No Google Gemini API key found in environment variables")
        genai.configure(api_key=self.api_key)
        generation_config = {
            "temperature": 0.5,
            "top_p": 1,
            "top_k": 1,
        }
        self.client = genai.GenerativeModel(
            model_name="gemini-pro-vision", generation_config=generation_config
        )
        print("Google Gemini Model initialized")

    def analyze_image(self, image_url):
        # Download the image from the URL
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Load the image into memory
        image = Image.open(BytesIO(response.content))  # Use PIL to open the image

        # Generate the response using the model
        prompt = [get_business_card_analysis_prompt(), image]
        response = self.client.generate_content(prompt)
        return response.text
