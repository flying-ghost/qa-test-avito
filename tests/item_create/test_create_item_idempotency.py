from helpers.data_helper import extract_item_id


def test_create_item_idempotency(items_client):
    seller_id = 995995
    payload = {
        "name": "Дубль",
        "price": 300,
        "sellerID": seller_id,
        "statistics": {
            "likes": 15,
            "viewCount": 4,
            "contacts": 45
        }
    }

    # первый запрос
    response1 = items_client.create_item(payload)
    item_id1 = extract_item_id(response1)
    assert response1.status_code in (200, 201)
    assert item_id1 is not None

    # второй запрос
    response2 = items_client.create_item(payload)
    item_id2 = extract_item_id(response2)
    assert response2.status_code in (200, 201)
    assert item_id2 is not None

    assert item_id1 != item_id2
