from src.agents.architecture_diagram import run_agent
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    image_path = "temp/4c180a9f-5347-46fe-93fd-31f879e6df79.png"
    run_agent(image_path)
