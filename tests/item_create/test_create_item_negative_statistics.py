from helpers.data_helper import generate_seller_id


def test_create_item_negative_statistics(items_client):
    seller_id = generate_seller_id()
    payload = {
        "name": "Тест",
        "price": 98,
        "sellerID": seller_id,
        "statistics": {
            "likes": -15,
            "viewCount": -4,
            "contacts": -45
        }
    }

    response = items_client.create_item(payload)

    assert response.status_code == 400
