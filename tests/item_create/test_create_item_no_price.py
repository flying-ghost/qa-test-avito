from helpers.data_helper import generate_seller_id


def test_create_item_no_price(items_client):

    seller_id = generate_seller_id()
    payload = {
        "name": "Тест",
        "sellerID": seller_id,
        "statistics": {
            "likes": 15,
            "viewCount": 4,
            "contacts": 45
        }
    }

    response = items_client.create_item(payload)

    assert response.status_code == 400
