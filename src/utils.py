import json
import os
import re

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def normalize_money(text):
    match = re.search(r"\$[\d,]+", text)
    return match.group() if match else text


def clean_output(text):
    text = text.strip()
    if len(text) > 100:
        return "Not Found"
    return text


def normalize_output(field, value):
    match = re.search(r"\$[\d,]+", value)
    if match:
        value = match.group()

    if field == "Governing Law" and "Delaware" in value:
        return "State of Delaware"

    return value