import base64
import io, requests
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from src.helpers.LLM import LLM
from src.helpers.get_prompt import get_prompt
from src.helpers.convert_base64_image import convert_base64_image
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import re


@tool
def generate_new_diagram_report(
    stride_report: str, architecture_diagram_path: str
) -> str:
    """
    Generates a new architecture diagram based on the STRIDE threat model report.

    This tool takes the path of an application's architecture diagram and its STRIDE report as input and
    generates a new architecture diagram that fixes the identified threats and vulnerabilities.

    Args:
        stride_report (str): A string containing the STRIDE threat model report.
        architecture_diagram_path (str): The path to the original architecture diagram.

    Returns:
        str: A string containing the new architecture diagram report, if not exists will return "Ocorreu um erro ao gerar o diagrama".
    """
    prompt = get_prompt(
        current_path=Path(__file__).parent,
        file_name="generate_new_diagram_report.md",
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
    model = LLM.call_gemini_model("gemini-2.5-flash")
    response = model.invoke(messages)
    return response


@tool
def generate_new_diagram_image(mermaid_diagram_code: str):
    """
    Generates a new architecture diagram image based on the provided diagram report.

    Args:
        mermaid_diagram_code (str): A string containing the Mermaid code for the new architecture diagram.

    Returns:
        str: A new architecture diagram, if not exists will return "Ocorreu um erro ao gerar o diagrama".
    """

    prompt = get_prompt(
        current_path=Path(__file__).parent,
        file_name="generate_new_diagram_image.md",
    )

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(
            content=f"Valide se o código mermaid a seguir é válido: {mermaid_diagram_code}, se não for aplique as correções necessárias e retorne o código corrigido."
        ),
    ]

    model = LLM.call_gemini_model("gemini-2.5-flash")

    model = LLM.call_gemini_model("gemini-2.5-flash")
    response = model.invoke(messages)
    print(response)
    return response
