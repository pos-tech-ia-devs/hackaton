from src.agents.architecture_diagram import run_agent
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    image_path = "resources/aws.png"
    run_agent(image_path)
