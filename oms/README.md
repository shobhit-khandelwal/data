# Order Management System (OMS)

This is a demonstration Order Management System that integrates with multiple
mock e-commerce platforms. It exposes a simple REST API using FastAPI.

## Features

- Retrieve quotes for items from Amazon, eBay, and Walmart connectors.
- Place orders on these platforms using stored credentials.
- In-memory order storage and simple credential management.

**Note:** The connectors are mock implementations and do not contact real
services. Encryption of credentials is simplified and should not be used in
production.

## Setup

1. Install Python 3.11 (already available in this environment).
2. Install dependencies (FastAPI and pytest are already available in this environment):
   ```bash
   pip install fastapi pytest  # if not already installed
   ```
   If the environment lacks network access, ensure these packages are present.

## Running the API

```bash
uvicorn oms.app:app --reload
```

## API Endpoints

### `POST /quotes`
Request body:
```json
{
  "items": ["ITEM1", "ITEM2"],
  "platforms": ["amazon", "ebay", "walmart"]
}
```

Response contains quote information for each item/platform pair.

### `POST /orders`
Request body:
```json
{
  "platform": "amazon",
  "item_id": "ITEM1",
  "credentials_id": "cred1",
  "shipping_address": "123 Example St"
}
```

Returns the placed order with an `order_id` that can be queried later.

### `GET /orders/<order_id>`
Returns order details.

## Testing

Run tests with `pytest`:
```bash
pytest oms/tests
```
