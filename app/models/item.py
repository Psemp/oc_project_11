from app.models.position_nt import Position


class Item:

    def __init__(self, name: str, item_x: int, item_y: int, identifier: str):
        self.name = name
        self.gathered = False
        self.position = Position(x_axis=item_x, y_axis=item_y)
        self.identifier = identifier

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
