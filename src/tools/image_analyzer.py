from PIL import Image
from langchain_community.tools import tool
from src.helpers.LLM import LLM, MODELS
from src.helpers.format_json import format_json
from src.helpers.get_prompt import get_prompt
from src.helpers.convert_base64_image import convert_base64_image
from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path


@tool
def analyze_image(image_path: str) -> str:
    """
    Analyzes a system architecture diagram image and returns a JSON representation.
    This tool takes the file path of an image, analyzes its components, containers,
    and data flows, and returns a structured JSON object describing the architecture.
    Args:
      image_path(str): The path of the image to be analyzed.
    Returns:
      str: A JSON string object with information about the image, or an error message.
    """
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return f"Error: Image file not found at path: {image_path}"
    except Exception as e:
        return f"Error: Could not open or process the image. Details: {e}"

    image_uri = convert_base64_image(img)
    model = LLM.call_gemini_model(MODELS.pro.value)

    prompt = get_prompt(
        current_path=Path(__file__).parent, file_name="analyze_image.md"
    )

    if not prompt:
        return "Error: The system prompt file 'analyze_image.md' was not found in the expected location."
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=[{"type": "image_url", "image_url": image_uri}]),
    ]

    response = model.invoke(messages)
    json_response = format_json(response.content)
    return json_response
