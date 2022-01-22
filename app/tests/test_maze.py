from app.models.map import Map
from app.scripts.maze import get_shapes

def test_shapes():
    shapes = get_shapes()
    assert isinstance(shapes, dict)
    for key in shapes.keys():
        assert isinstance(key, int)

def test_map_creation():
    test_map = Map(20, 20)
    assert len(test_map.box) == 20
    assert len(test_map.box[0]) == 20
