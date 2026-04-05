from helpers.data_helper import generate_seller_id


def test_get_for_seller_ads(items_client):
    seller_id = generate_seller_id()
    payload_1 = {
        "name": "Тест 1",
        "price": 100,
        "sellerID": seller_id,
        "statistics": {"likes": 1, "viewCount": 2, "contacts": 3}
    }
    payload_2 = {
        "name": "Тест 2",
        "price": 200,
        "sellerID": seller_id,
        "statistics": {"likes": 2, "viewCount": 3, "contacts": 4}
    }
    items_client.create_item(payload_1)
    items_client.create_item(payload_2)

    response = items_client.get_items_by_seller(seller_id)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 1
