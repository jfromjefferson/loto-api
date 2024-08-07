
class Calculator:
    def __init__(self, game_id: int, game_count: int):
        self.game_id = game_id
        self.game_count = game_count

    def calculate(self) -> float:
        if self.game_id == 1:
            return 3.00 * self.game_count

        return 0
