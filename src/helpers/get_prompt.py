from pathlib import Path


def get_prompt(current_path: Path, file_name: str):
    try:
        prompt_path = current_path / "prompts" / file_name
        with open(prompt_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The system prompt file '{file_name}' was not found in the expected location."
