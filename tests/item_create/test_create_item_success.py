from helpers.data_helper import generate_item_payload, extract_item_id


def test_create_item_success(items_client):

    payload = generate_item_payload()

    response = items_client.create_item(payload)
    item_id = extract_item_id(response)

    assert response.status_code in (200, 201)
    assert item_id is not None
