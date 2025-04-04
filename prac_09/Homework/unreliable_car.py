"""
CP1404/CP5632 Practical
UnreliableCar class, derived from Car
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable car that only drives depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability  # Set reliability percentage

    def drive(self, distance):
        """Only drive if a random number is less than the reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)  # Drive as normal
        return 0  # Car fails to drive
