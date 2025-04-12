"""Band class for CP1404"""

class Band:
    """Band class representing a group of musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician in the band is playing."""
        return "\n".join(musician.play() for musician in self.musicians)
