def test_create_item_no_sellerid(items_client):
    payload = {
        "name": "Тест",
        "price": 50000,
        "statistics": {
            "likes": 15,
            "viewCount": 4,
            "contacts": 45
        }
    }

    response = items_client.create_item(payload)

    assert response.status_code == 400
