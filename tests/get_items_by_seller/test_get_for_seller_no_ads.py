from helpers.data_helper import generate_seller_id


def test_get_for_seller_no_ads(items_client):
    seller_id = generate_seller_id()

    response = items_client.get_items_by_seller(seller_id)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data == []
