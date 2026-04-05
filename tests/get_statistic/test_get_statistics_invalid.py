def test_get_statistics_invalid_id(items_client):
    response = items_client.get_statistic("1000000")

    assert response.status_code == 400
