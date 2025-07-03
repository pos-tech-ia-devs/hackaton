from PIL import Image
import base64
import io
from langchain_community.tools import tool
from pathlib import Path
from src.helpers.LLM import LLM
from src.helpers.format_json import format_json
from langchain_core.messages import HumanMessage, SystemMessage


def convert_base64_image(img):
    buffered = io.BytesIO()
    image_format = img.format or "PNG"
    img.save(buffered, format=image_format)
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    image_uri = f"data:image/{image_format.lower()};base64,{img_base64}"
    return image_uri


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
    model = LLM.call_gemini_model("gemini-2.5-pro")

    try:
        script_dir = Path(__file__).parent
        prompt_path = script_dir / "prompts" / "analyze_image.md"
        with open(prompt_path, "r") as file:
            prompt = file.read()
    except FileNotFoundError:
        return "Error: The system prompt file 'analyze_image.md' was not found in the expected location."

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=[{"type": "image_url", "image_url": image_uri}]),
    ]

    response = model.invoke(messages)
    json_response = format_json(response.content)
    return json_response
