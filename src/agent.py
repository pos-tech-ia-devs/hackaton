from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_functions_agent
from .tools.toolkit import get_toolkit
from .helpers.LLM import LLM


def run_agent(image_path):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """ 
                You are an AI assistant.
                Use your tools to complete the following task.
                You have access to the following tools: analyze_image
                You should response in markdown format.
                """,
            ),
            MessagesPlaceholder("history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    toolkit = get_toolkit()
    agent_llm = LLM.call_gemini_model("gemini-2.5-flash")
    agent = create_openai_functions_agent(agent_llm, toolkit, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=toolkit, verbose=True)

    response = agent_executor.invoke({"input": image_path})
    print(response["output"])


if __name__ == "__main__":
    image_path = "resources/aws.png"
    run_agent(image_path)
