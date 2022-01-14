class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Distance from start
        self.h = 0  # Heuristic
        self.f = 0  # Total estimated cost

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f
