def test_get_items_seller_invalid(items_client):

    response = items_client.get_items_by_seller("abc")

    assert response.status_code == 400
