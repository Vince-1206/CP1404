"""
CP1404/CP5632 Practical
SilverServiceTaxi class, derived from Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more luxurious taxi service with a higher fare rate and a flagfall charge."""

    flagfall = 4.50  # Class variable for the extra charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness  # Scale the base price by fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
