import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 10, 2) == 12