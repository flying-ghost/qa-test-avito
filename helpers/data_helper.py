import random
import re

def generate_item_payload(name=None, seller_id=None):
    return {
        "name": name or "Test",
        "price": 10000,  # фиксированная цена
        "sellerID": seller_id if seller_id is not None else random.randint(111111, 999999),
        "statistics": {
            "likes": 15,
            "viewCount": 4,
            "contacts": 45
        }
    }

def generate_seller_id(start=111111, end=999999):
    return random.randint(start, end)

def extract_item_id(response):
    match = re.search(
        r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        response.text
    )
    return match.group(0) if match else None