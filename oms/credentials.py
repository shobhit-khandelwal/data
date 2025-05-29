"""Simple credential storage using base64 encoding as placeholder encryption."""
import base64
import json
import os
from typing import Dict

CREDENTIAL_FILE = os.path.join(os.path.dirname(__file__), "credentials.json")


def load_credentials() -> Dict[str, dict]:
    if not os.path.exists(CREDENTIAL_FILE):
        return {}
    with open(CREDENTIAL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_credentials(creds: Dict[str, dict]):
    with open(CREDENTIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(creds, f)


def add_credential(cred_id: str, data: dict):
    creds = load_credentials()
    encoded = base64.b64encode(json.dumps(data).encode()).decode()
    creds[cred_id] = encoded
    save_credentials(creds)


def get_credential(cred_id: str) -> dict | None:
    creds = load_credentials()
    encoded = creds.get(cred_id)
    if not encoded:
        return None
    decoded = base64.b64decode(encoded).decode()
    return json.loads(decoded)


def remove_credential(cred_id: str):
    creds = load_credentials()
    if cred_id in creds:
        creds.pop(cred_id)
        save_credentials(creds)
