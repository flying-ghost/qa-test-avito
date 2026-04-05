from helpers.data_helper import generate_seller_id, extract_item_id


def test_get_statistics(items_client):
    payload = {
        "name": "Тест",
        "price": 1000,
        "sellerID": generate_seller_id(),
        "statistics": {
            "likes": 10,
            "viewCount": 5,
            "contacts": 2
        }
    }
    create_response = items_client.create_item(payload)
    assert create_response.status_code in (200, 201)
    item_id = extract_item_id(create_response)
    assert item_id is not None

    stat_response = items_client.get_statistic(item_id)
    assert stat_response.status_code == 200

    data = stat_response.json()[0]
    assert "likes" in data
    assert "viewCount" in data
    assert "contacts" in data
