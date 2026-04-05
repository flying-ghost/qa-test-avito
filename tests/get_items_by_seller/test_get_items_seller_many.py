def test_get_items_seller_many(items_client):

    huge_seller_id = 10_000_000_000_000_000_000
    response = items_client.get_items_by_seller(huge_seller_id)

    assert response.status_code == 400
