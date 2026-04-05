from helpers.data_helper import generate_seller_id, extract_item_id


def test_get_item_id(items_client):
    payload = {
        "name": "Тест GET",
        "price": 500,
        "sellerID": generate_seller_id(),
        "statistics": {
            "likes": 5,
            "viewCount": 2,
            "contacts": 3
        }
    }
    create_response = items_client.create_item(payload)
    assert create_response.status_code in (200, 201)
    item_id = extract_item_id(create_response)
    assert item_id is not None

    get_response = items_client.get_item(item_id)
    assert get_response.status_code == 200
