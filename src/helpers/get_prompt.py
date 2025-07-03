from pathlib import Path


def get_prompt(current_path: Path, file_name: str):
    try:
        prompt_path = current_path / "prompts" / file_name
        with open(prompt_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The system prompt file 'architecture_diagram.md' was not found in the expected location."
