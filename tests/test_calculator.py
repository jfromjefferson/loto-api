from utils.calculator import Calculator


def test_calculate_valid_game_id():
    calculator = Calculator(game_id=1, game_count=5)
    result = calculator.calculate()

    assert result == 15.00


def test_calculate_invalid_game_id():
    calculator = Calculator(game_id=2, game_count=5)
    result = calculator.calculate()

    assert result == 0
