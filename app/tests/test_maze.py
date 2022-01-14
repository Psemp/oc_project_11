from app.models.map import Map


def test_map_creation():
    test_map = Map(20, 20)
    assert len(test_map.box) == 20
    assert len(test_map.box[0]) == 20
