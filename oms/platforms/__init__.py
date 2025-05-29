from .amazon import AmazonConnector
from .ebay import EbayConnector
from .walmart import WalmartConnector


CONNECTORS = {
    "amazon": AmazonConnector(),
    "ebay": EbayConnector(),
    "walmart": WalmartConnector(),
}


def get_connector(name: str):
    return CONNECTORS.get(name)
