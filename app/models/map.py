from app.scripts.maze import mazify
import numpy as np


class Map:

    def __init__(self, user_height: int, user_length: int):
        self.map_x = 0
        self.map_y = 0
        self.length = user_length
        self.height = user_height
        self.map_increment = 32

        def make_box(self):
            cell_amount = user_length * user_height
            one_d = [0 for cell in range(cell_amount)]
            self.box = np.reshape(one_d, (user_height, user_length))
            for row in self.box:
                row[0] = 1
                row[-1] = 1

            row_filled_1 = [1 for cell in self.box[1]]
            self.box[0] = row_filled_1
            self.box[-1] = row_filled_1
            return self.box

        self.box = make_box(self)
        self.box = mazify(self.box)

    def make_map(self):
        """reads the box and classifies whats a wall (1s) and floors (0s),
        appends them to their respective list and increment of 32 each time it
        does (width of sprites), resetting at row*32 (EOL)"""
        self.floors = []
        self.walls = []

        row_idx = 0
        for row in self.box:
            cell_idx = 0
            for cell in row:
                if cell != 1 or cell == 0:
                    self.floors.append((cell_idx * 32, row_idx * 32))
                elif cell == 1:
                    self.walls.append((cell_idx * 32, row_idx * 32))
                cell_idx += 1
            row_idx += 1

    def insert(self, identifier, position):
        self.box[position.y_axis][position.x_axis] = identifier
