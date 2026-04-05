from helpers.data_helper import generate_seller_id


def test_create_item_no_statistics(items_client):
    seller_id = generate_seller_id()
    payload = {
        "name": "Тест",
        "price": 1000,
        "sellerID": seller_id
    }

    response = items_client.create_item(payload)

    assert response.status_code == 400
