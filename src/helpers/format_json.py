import json
import re


def format_json(chain_output):
    match = re.search(r"\[\s*\{.*\}\s*\]", chain_output, re.DOTALL)
    if match:
        json_str = match.group(0).strip()
        return json_str
    else:
        print("❌ No JSON found")

    return None
