from PIL import Image
import base64
import io
from langchain_community.tools import tool
from src.helpers import LLM, format_json
from langchain_core.messages import HumanMessage, SystemMessage


def convert_base64_image(img):
    buffered = io.BytesIO()
    image_format = img.format or "PNG"
    img.save(buffered, format=image_format)
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    image_uri = f"data:image/{image_format.lower()};base64,{img_base64}"
    return image_uri


@tool
def analyze_image(image_path):
    """
    You are an image analyzer, your task is to receive the path of an image and return a JSON with information about the image.
    The image is a system architecture image, and you should analyze the image and return a JSON with information about the image.

    The JSON should have the following structure:
    Args:
      image_path(str): The path of the image to be analyzed.

    Returns:
      response(str): A JSON with information about the image.
    """
    img = Image.open(image_path)
    image_uri = convert_base64_image(img)
    model = LLM.load_ollama_model("gemini-2.5-flash")

    with open("./prompts/analyze_image.md", "r") as file:
        prompt = file.read()

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(
            content=[
                {"type": "image_url", "image_url": image_uri},
            ]
        ),
    ]

    response = model.invoke(messages)

    json = format_json(response)
    return json
