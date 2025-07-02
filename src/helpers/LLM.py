from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class LLM:
    @staticmethod
    def call_gemini_model(model_name, temperature=0):
        model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=temperature,
        )
        return model

    @staticmethod
    def call_open_ai_model(temperature=0.5):
        model = ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL"),
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=temperature,
        )
        return model
