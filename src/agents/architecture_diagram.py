from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from src.tools.toolkit import get_toolkit
from src.helpers.LLM import LLM
from helpers.get_prompt import get_prompt
from pathlib import Path


def run_agent(image_path: str, api_key: str | None = None):
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

        agent_llm = LLM.call_gemini_model(
            model_name="gemini-2.5-flash",
            temperature=0,
            api_key=api_key,
        )
        agent = create_tool_calling_agent(agent_llm, toolkit, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)

        response = agent_executor.invoke(
            {
                "input": f"Analise a imagem desse caminho: {image_path}, retorne um relatório stride apontando vulnerabilidades e ameaças, também um novo diagrama corrigindo as vulnerabilidades encontradas."
            }
        )
        if response.get("output"):
            return response["output"]
        else:
            print("No output found in the response.")

    except Exception as e:
        print(f"An error occurred: {e}")
