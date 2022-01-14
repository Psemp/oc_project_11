class Couplepos:  # Might be useless
    def __init__(self, start_position, goal_position) -> None:
        self.start_position = start_position
        self.goal_position = goal_position

    def __repr__(self) -> str:
        return f"{self.start_position} - {self.goal_position}"
