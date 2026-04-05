import requests
from constants.constants import BASE_URL, DEFAULT_TIMEOUT


class ItemsClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = DEFAULT_TIMEOUT

    def create_item(self, payload):
        return requests.post(
            f"{self.base_url}/api/1/item",
            json=payload,
            timeout=self.timeout
        )

    def get_item(self, item_id):
        return requests.get(
            f"{self.base_url}/api/1/item/{item_id}",
            timeout=self.timeout
        )

    def get_items_by_seller(self, seller_id):
        return requests.get(
            f"{self.base_url}/api/1/{seller_id}/item",
            timeout=self.timeout
        )

    def get_statistic(self, item_id):
        return requests.get(
            f"{self.base_url}/api/1/statistic/{item_id}",
            timeout=self.timeout
        )
