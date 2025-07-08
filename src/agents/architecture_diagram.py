from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from src.tools.toolkit import get_toolkit
from src.helpers.LLM import LLM, MODELS
from helpers.get_prompt import get_prompt
from pathlib import Path


def run_agent(image_path: str, debug_mode: bool = False):
    try:
        orchestrator_prompt = get_prompt(
            current_path=Path(__file__).parent, file_name="architecture_diagram.md"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", orchestrator_prompt),
                MessagesPlaceholder("history", optional=True),
                ("user", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )

        toolkit = get_toolkit()

        agent_llm = LLM.call_gemini_model(model_name=MODELS.flash.value)
        agent = create_tool_calling_agent(agent_llm, toolkit, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=debug_mode)

        response = agent_executor.invoke(
            {
                "input": f"""
                    Perform the following security analysis on the provided image:

                    1. First, analyze the architecture in the path diagram: {image_path}.
                    2. Based on the analysis, generate a complete threat report using the STRIDE methodology.
                    3. Next, create a remediation report detailing the mitigations for each vulnerability found.
                    4. Finally, generate a new image Mermaid code that incorporates all the proposed remediations.
                    5. Returns everything in portuguese (pt-BR)
                    """
            }
        )
        if response.get("output"):
            return response["output"]
        else:
            print("No output found in the response.")

    except Exception as e:
        print(f"An error occurred: {e}")
