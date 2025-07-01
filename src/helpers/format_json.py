import json
import re


def format_json(chain_output):
    match = re.search(r"\[\s*\{.*\}\s*\]", chain_output, re.DOTALL)
    if match:
        json_str = match.group(0).strip()
        try:
            array_obj = json.loads(json_str)
            return array_obj

        except json.JSONDecodeError as e:
            print("❌ JSON Decode error:", e)

    else:
        print("❌ No JSON found")

    return None
