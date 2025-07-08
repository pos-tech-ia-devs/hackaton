from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from src.helpers.LLM import LLM, MODELS
from src.helpers.get_prompt import get_prompt
from pathlib import Path


@tool
def stride(architecture_json: str):
    """
    Executes a STRIDE threat modeling analysis on a JSON-defined architecture.

    This tool performs a comprehensive security analysis of a system architecture
    provided as a hierarchical JSON graph. It interprets the components, data
    flows, and infers trust boundaries from the graph structure. The analysis
    is framed using the STRIDE methodology (Spoofing, Tampering, Repudiation,
    Information Disclosure, Denial of Service, Elevation of Privilege).

    The function is designed to act as an expert security architect, providing
    a detailed report that identifies potential threats, explains their
    relevance to the specific architecture, and suggests actionable mitigations.

    Args:
        architecture_json (str): A JSON string representing the system
            architecture. It must conform to the specified graph structure,
            containing 'nodes' and 'edges' keys.

    Returns:
        str: A string formatted in Markdown containing the complete threat
            modeling report. The report details identified threats and
            suggested mitigations for each of the six STRIDE categories.
    """

    prompt = get_prompt(current_path=Path(__file__).parent, file_name="stride.md")
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=architecture_json),
    ]

    model = LLM.call_gemini_model(MODELS.pro.value, temperature=0.3)
    response = model.invoke(messages)
    return response
