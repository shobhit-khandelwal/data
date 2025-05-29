"""In-memory order store."""
import uuid
from typing import Dict

ORDERS: Dict[str, dict] = {}


def create_order(data: dict) -> dict:
    order_id = str(uuid.uuid4())
    data["order_id"] = order_id
    ORDERS[order_id] = data
    return data


def get_order(order_id: str) -> dict | None:
    return ORDERS.get(order_id)
