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

    def can_move(self, destination, maze_array):
        return maze_array[destination.x_axis][destination.y_axis] != 1

    def move_to(self, new_x, new_y, maze):
        """replaces identifier of char on map by floor,"""
        destination = Position(x_axis=new_x, y_axis=new_y)
        old_pos = Position(x_axis=self.x_now, y_axis=self.y_now)
        if self.can_move(destination=destination, maze_array=maze.box):
            maze.update_pos(self.map_identifier, old_pos, destination)
            self.x_now = destination.x_axis
            self.y_now = destination.y_axis

    def show_char(self):
        if not self.alive:
            self.show = False
        else:
            self.show = True

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
