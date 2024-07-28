import pytest
from utils.generator import Generator


def test_generate_random_numbers():
    generator = Generator()
    numbers, mirror_numbers = generator.generate_random_numbers()

    assert len(numbers) == 15
    assert len(mirror_numbers) == 15
    assert len(numbers + mirror_numbers) == 30
    assert all(number in generator.lotofacil_numbers for number in numbers)
    assert all(number in generator.lotofacil_numbers for number in mirror_numbers)
    assert len(set(numbers)) == 15  # Ensure numbers are unique
    assert len(set(mirror_numbers)) == 15  # Ensure mirror numbers are unique


def test_generate_random_numbers_10_valid_choices():
    generator = Generator()

    choices = [8, 4, 1, 23, 15]
    numbers, mirror_numbers = generator.generate_random_numbers_10(choices=choices)

    assert len(numbers) == 15
    assert len(mirror_numbers) == 15
    assert all(number in generator.lotofacil_numbers for number in numbers)
    assert all(number in generator.lotofacil_numbers for number in mirror_numbers)
    assert len(set(numbers)) == 15  # Ensure numbers are unique
    assert len(set(mirror_numbers)) == 15  # Ensure mirror numbers are unique
    assert all(choice in numbers for choice in choices)  # Ensure choices are in the numbers list


def test_generate_random_numbers_10_invalid_choices():
    generator = Generator()
    invalid_choices = [1, 2, 3, 4, 26]  # 26 is not a valid number

    with pytest.raises(ValueError) as excinfo:
        generator.generate_random_numbers_10(invalid_choices)

    assert "Numbers [26] are not valid" in str(excinfo.value)
