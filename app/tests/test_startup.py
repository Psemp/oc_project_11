from app.scripts.startup import startup
from app.models.map import Map
from app.models.character import Character
from app.models.item import Item


def test_startup():
    test_assets = startup()
    test_maze = test_assets["maze"]
    test_items = test_assets["items"]
    test_characters = test_assets["characters"]

    for character in test_characters:
        assert isinstance(character, Character)

    for item in test_items:
        assert isinstance(item, Item)

    assert isinstance(test_maze, Map)

    # Assert character[0] <- Ford in line 1
    assert test_characters[0].position.y_axis == 1

    # Assert character[1] <- Bernard in penultimate line
    assert test_characters[1].position.y_axis == len(test_maze.box) - 2
