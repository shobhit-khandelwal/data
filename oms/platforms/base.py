class PlatformConnector:
    """Base class for platform connectors."""
    name = "base"

    def get_quote(self, item_id: str) -> dict:
        raise NotImplementedError

    def place_order(self, item_id: str, credentials: dict, shipping_address: str) -> dict:
        raise NotImplementedError
