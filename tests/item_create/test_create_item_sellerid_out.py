

def test_create_item_sellerid_out(items_client):

    payload = {
        "name": "Тест",
        "price": 1000,
        "sellerID": 10000000000000000000,
        "statistics": {
            "likes": 15,
            "viewCount": 4,
            "contacts": 45
        }
    }

    response = items_client.create_item(payload)

    assert response.status_code == 400
