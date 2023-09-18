class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def intersects(self, other):
        return not (
            other.x + other.width < self.x or other.x > self.x + self.width
        ) and not (other.y + other.height < self.y or other.y > self.y + self.height)
