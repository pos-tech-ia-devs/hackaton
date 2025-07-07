from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from src.helpers.LLM import LLM, MODELS
from src.helpers.get_prompt import get_prompt
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import io, requests
import base64
import re
from src.helpers.convert_base64_image import convert_base64_image


@tool
def generate_mermaid_diagram(fixed_report: str, architecture_diagram_path: str):
    """
    Generates a new architecture diagram image based on the provided fixed report.

    Args:
        fixed_report (str): the report containing all suggested improvements
        architecture_diagram_path (str): The path to the original architecture diagram.

    Returns:
        str: Mermaid code for the new architecture diagram.
    """

    prompt = get_prompt(
        current_path=Path(__file__).parent,
        file_name="mermaid_diagram.md",
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
        HumanMessage(content=[{"type": "image_url", "image_url": image_uri}]),
        HumanMessage(
            content=f"Generate a mermaid based in the following report: {fixed_report} and the original diagram image"
        ),
    ]

    model = LLM.call_gemini_model(MODELS.flash.value)
    response = model.invoke(messages)
    content = response.content
    print("content:", content)

    regex = r"```mermaid\s*\n(.*?)\n```"
    match = re.search(regex, content, re.DOTALL)
    if match:
        codigo_extraido = match.group(1)
        content = codigo_extraido.strip()

    try:
        graphbytes = content.encode("utf8")
        base64_bytes = base64.urlsafe_b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")

        image_uri = "https://mermaid.ink/img/" + base64_string
        img = Image.open(io.BytesIO(requests.get(image_uri).content))

        plt.figure(figsize=(10, 8))
        plt.axis("off")
        plt.imshow(img)
        uri = "./temp/new_diagram.png"
        plt.savefig(uri, bbox_inches="tight", pad_inches=0, dpi=600)
        plt.close()
    except Exception as e:
        print("Erro ao gerar a image")

    return content
