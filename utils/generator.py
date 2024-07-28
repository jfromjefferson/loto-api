import random
from typing import Tuple, Any, List

from .numbers import LOTOFACIL_NUMBERS


class Generator:
    def __init__(self):
        self.lotofacil_numbers = [*LOTOFACIL_NUMBERS]

    def generate_random_numbers(self) -> tuple[list[int], list[int]]:
        """
        Generate a list of 15 random numbers between 1 and 25
        """
        numbers = random.sample(self.lotofacil_numbers, 15)
        mirror_numbers = [number for number in self.lotofacil_numbers if number not in numbers] + random.sample(numbers, 5)

        numbers.sort()
        mirror_numbers.sort()

        return numbers, mirror_numbers

    def generate_random_numbers_10(self, choices: list[int]) -> tuple[list[int], list[int]]:
        """
        Generate a list of 10 random numbers between 1 and 25, considering the choices
        """

        not_in_lotofacil_numbers = [number for number in choices if number not in self.lotofacil_numbers]

        if not_in_lotofacil_numbers:
            raise ValueError(f"Numbers {not_in_lotofacil_numbers} are not valid")

        numbers_without_choices = [number for number in self.lotofacil_numbers if number not in choices]
        numbers = random.sample(numbers_without_choices, 10) + choices
        mirror_numbers = [number for number in numbers_without_choices if number not in numbers] + choices

        numbers.sort()
        mirror_numbers.sort()

        return numbers, mirror_numbers
