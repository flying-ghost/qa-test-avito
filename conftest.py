import pytest
from clients.items_client import ItemsClient


@pytest.fixture
def items_client():
    return ItemsClient()