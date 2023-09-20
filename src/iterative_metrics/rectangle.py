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

    def contains(self, other):
        is_contained_horizontally = (
            self.x <= other.x <= other.x + other.width <= self.x + self.width
        )
        is_contained_vertically = (
            self.y <= other.y <= other.y + other.height <= self.y + self.height
        )
        return is_contained_horizontally and is_contained_vertically

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
