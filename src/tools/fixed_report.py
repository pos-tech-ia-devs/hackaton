from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from src.helpers.LLM import LLM, MODELS
from src.helpers.get_prompt import get_prompt
from src.helpers.convert_base64_image import convert_base64_image
from PIL import Image
from pathlib import Path


@tool
def generate_fixed_report(stride_report: str, architecture_diagram_path: str) -> str:
    """
    Generate a report correcting the points highlighted in the provided STRIDE report
    This tool takes the path of an application's architecture diagram and its STRIDE report as input and generates a new relatório that fixes the identified threats and vulnerabilities.

    Args:
        stride_report (str): A string containing the STRIDE threat model report.
        architecture_diagram_path (str): The path to the original architecture diagram.

    Returns:
        str: A string containing the new report, if not exists will return "Ocorreu um erro ao gerar o relatório de melhoria".
    """
    prompt = get_prompt(
        current_path=Path(__file__).parent,
        file_name="fixed_report.md",
    )

    try:
        img = Image.open(architecture_diagram_path)
    except FileNotFoundError:
        return f"Error: Image file not found at path: {architecture_diagram_path}"
    except Exception as e:
        return f"Error: Could not open or process the image. Details: {e}"
    image_uri = convert_base64_image(img)

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=stride_report),
        HumanMessage(content=[{"type": "image_url", "image_url": image_uri}]),
    ]
    model = LLM.call_gemini_model(MODELS.flash.value, temperature=0.3)
    response = model.invoke(messages)
    return response
