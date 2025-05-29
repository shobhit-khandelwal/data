import json
from oms.app import quotes as quotes_handler, orders as orders_handler, order_status as order_status_handler, QuoteRequest, OrderRequest
from oms.credentials import add_credential, remove_credential


def setup_module(module):
    add_credential("cred1", {"username": "user", "password": "pass"})


def teardown_module(module):
    remove_credential("cred1")


def test_quotes():
    # Call handler directly instead of HTTP request
    req = QuoteRequest(items=["A1"], platforms=["amazon", "ebay", "walmart"])
    data = quotes_handler(req)
    assert "quotes" in data
    assert len(data["quotes"]) == 3


def test_order_flow():
    req = OrderRequest(
        platform="amazon",
        item_id="A1",
        credentials_id="cred1",
        shipping_address="123",
    )
    order = orders_handler(req)
    oid = order["order_id"]
    data2 = order_status_handler(oid)
    assert data2["order_id"] == oid
