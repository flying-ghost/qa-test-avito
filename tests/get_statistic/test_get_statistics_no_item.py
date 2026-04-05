def test_get_statistics_no_item(items_client):
    response = items_client.get_statistic(
        "00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404
