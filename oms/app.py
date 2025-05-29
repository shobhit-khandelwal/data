from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .platforms import CONNECTORS, get_connector
from .credentials import get_credential
from .orders import create_order, get_order

app = FastAPI()


class QuoteRequest(BaseModel):
    items: list[str] = []
    platforms: list[str] | None = None


class OrderRequest(BaseModel):
    platform: str
    item_id: str
    credentials_id: str
    shipping_address: str = ""


@app.post("/quotes")
def quotes(req: QuoteRequest):
    items = req.items
    platforms = req.platforms or list(CONNECTORS.keys())
    responses = []
    errors = []
    for item in items:
        for platform in platforms:
            connector = get_connector(platform)
            if not connector:
                errors.append({"item_id": item, "platform": platform, "error": "unknown platform"})
                continue
            try:
                responses.append(connector.get_quote(item))
            except Exception as exc:  # pragma: no cover - unexpected errors
                errors.append({"item_id": item, "platform": platform, "error": str(exc)})
    return {"quotes": responses, "errors": errors}


@app.post("/orders")
def orders(req: OrderRequest):
    connector = get_connector(req.platform)
    if not connector:
        raise HTTPException(status_code=400, detail="unknown platform")
    creds = get_credential(req.credentials_id)
    if not creds:
        raise HTTPException(status_code=400, detail="credentials not found")
    result = connector.place_order(req.item_id, creds, req.shipping_address)
    order = create_order(result)
    return order


@app.get("/orders/{order_id}")
def order_status(order_id: str):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    return order


def create_app() -> FastAPI:
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
