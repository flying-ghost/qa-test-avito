def test_get_items_seller_10(items_client):

    response = items_client.get_items_by_seller(10)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
