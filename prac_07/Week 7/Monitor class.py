"""
model, width, and height

"""

class Monitor:
    def __init__(self, model: str, width: int, height: int):
        self.model = model
        self.width = width
        self.height = height
    def get_resolution(self) -> tuple:
        return self.width, self.height
    def get_total_pixels(self) -> int:
        return self.width * self.height
    def __eq__(self, other) -> bool:
        return self.width == other.width and self.height == other.height