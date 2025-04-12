"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence: capitalized and ending with a single period.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("welcome to CP1404")
    'Welcome to CP1404.'
    """
    phrase = phrase.strip()
    if not phrase.endswith("."):
        phrase += "."
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # test Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # test Car's fuel attribute (default and custom value)
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when a value is given"
    car = Car()
    assert car.fuel == 0, "Car does not default fuel to 0"


run_tests()

# Run doctests
doctest.testmod()
