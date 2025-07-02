from langchain_community.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path
from src.helpers.LLM import LLM


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
        architecture_json (dict): A dictionary representing the system
            architecture. It must conform to the specified graph structure,
            containing 'nodes' and 'edges' keys.

    Returns:
        str: A string formatted in Markdown containing the complete threat
            modeling report. The report details identified threats and
            suggested mitigations for each of the six STRIDE categories.
    """

    try:
        script_dir = Path(__file__).parent
        prompt_path = script_dir / "prompts" / "stride.md"
        with open(prompt_path, "r") as file:
            prompt = file.read()
    except FileNotFoundError:
        return "Error: The system prompt file 'analyze_image.md' was not found in the expected location."

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=architecture_json),
    ]

    model = LLM.call_gemini_model("gemini-2.5-pro")
    response = model.invoke(messages)
    return response
