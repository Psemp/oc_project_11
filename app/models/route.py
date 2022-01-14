import math


class Route:

    def __init__(self, path_list: list) -> None:
        self.path_list = path_list
        self.position_list = []
        self.pathway = []
        self.weight = math.inf

    def __repr__(self) -> str:
        return str(self.path_list)
