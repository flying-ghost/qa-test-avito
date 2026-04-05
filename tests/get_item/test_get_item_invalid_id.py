def test_get_item_invalid_id(items_client):
    invalid_id = "0000000"

    response = items_client.get_item(invalid_id)

    assert response.status_code == 400
