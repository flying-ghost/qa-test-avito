def assert_item_structure(item: dict):
    assert "id" in item
    assert "name" in item
    assert "price" in item
    assert "sellerId" in item
    assert "statistics" in item

    stats = item["statistics"]

    assert "likes" in stats
    assert "viewCount" in stats
    assert "contacts" in stats


def assert_statistic_structure(stat: dict):
    assert "likes" in stat
    assert "viewCount" in stat
    assert "contacts" in stat