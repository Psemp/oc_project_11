from app.models.position_nt import Position


class Character:

    def __init__(self, name: str, char_x: int, char_y: int, map_identifier: int, is_npc: bool):
        self.name = name
        self.position = Position(x_axis=char_x, y_axis=char_y)
        self.x_now = char_x
        self.y_now = char_y
        self.vel = 32  # For pygame
        self.alive = True
        self.npc = is_npc
        self.map_identifier = map_identifier

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
