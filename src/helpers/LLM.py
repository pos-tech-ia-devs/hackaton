from langchain_google_genai import ChatGoogleGenerativeAI


import os
from dotenv import load_dotenv

load_dotenv()


class LLM:
    @staticmethod
    def load_ollama_model(model_name, temperature=0):
        model = ChatGoogleGenerativeAI(
            model=model_name,
            base_url=os.getenv("GEMINI_API_KEY"),
            temperature=temperature,
        )
        return model
