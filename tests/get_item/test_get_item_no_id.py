def test_get_item_no_id(items_client):
    no_id = "00000000-0000-0000-0000-000000000000"

    response = items_client.get_item(no_id)

    assert response.status_code == 404
