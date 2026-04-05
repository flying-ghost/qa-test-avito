from helpers.data_helper import generate_seller_id, extract_item_id


def test_e2e_item(items_client):
    seller_id = generate_seller_id()

    payload = {
        "name": "E2E Test",
        "price": 1000,
        "sellerID": seller_id,
        "statistics": {
            "likes": 10,
            "viewCount": 5,
            "contacts": 3
        }
    }

    # Создание объявления
    create_response = items_client.create_item(payload)
    assert create_response.status_code in (200, 201)

    item_id = extract_item_id(create_response)
    assert item_id is not None

    get_response = items_client.get_item(item_id)
    assert get_response.status_code == 200

    data = get_response.json()
    if isinstance(data, list):
        data = data[0]

    assert data["id"] == item_id
    assert data["name"] == payload["name"]
    assert data["price"] == payload["price"]

    stat_response = items_client.get_statistic(item_id)
    assert stat_response.status_code == 200

    stat_data = stat_response.json()
    if isinstance(stat_data, list):
        stat_data = stat_data[0]

    assert stat_data["likes"] == payload["statistics"]["likes"]
    assert stat_data["viewCount"] == payload["statistics"]["viewCount"]
    assert stat_data["contacts"] == payload["statistics"]["contacts"]
