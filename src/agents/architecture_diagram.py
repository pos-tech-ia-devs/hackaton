from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from src.tools.toolkit import get_toolkit
from src.helpers.LLM import LLM
from pathlib import Path


def get_prompt():
    try:
        script_dir = Path(__file__).parent
        prompt_path = script_dir / "prompts" / "architecture_diagram.md"
        with open(prompt_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The system prompt file 'architecture_diagram.md' was not found in the expected location."


def run_agent(image_path: str):
    try:
        orchestrator_prompt = get_prompt()
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", orchestrator_prompt),
                MessagesPlaceholder("history", optional=True),
                ("user", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )

        toolkit = get_toolkit()
        agent_llm = LLM.call_gemini_model(
            model_name="gemini-2.5-flash",
            temperature=0,
        )
        agent = create_tool_calling_agent(agent_llm, toolkit, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)

        response = agent_executor.invoke(
            {
                "input": f"Analise a imagem desse caminho: {image_path}, retorne um relatório stride apontando vulnerabilidades e ameaças."
            }
        )
        print(response)
        return response["output"]

    except Exception as e:
        print(f"An error occurred: {e}")
