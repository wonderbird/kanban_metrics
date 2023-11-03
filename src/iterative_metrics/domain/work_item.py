from iterative_metrics.domain.rectangle import Rectangle


class WorkItem:
    def __init__(self, bounding_rectangle: Rectangle) -> None:
        self.bounding_rectangle = bounding_rectangle

    def __repr__(self):
        return f"WorkItem(bounding_rectangle={self.bounding_rectangle})"

    @property
    def height(self) -> int:
        return self.bounding_rectangle.height

    @property
    def width(self) -> int:
        return self.bounding_rectangle.width
