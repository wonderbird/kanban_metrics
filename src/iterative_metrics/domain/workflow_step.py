from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_items import WorkItems


class WorkflowStep:
    def __init__(self, bounding_rectangle: Rectangle) -> None:
        self.bounding_rectangle = bounding_rectangle
        self.number_of_work_items = 0

    def contains(self, work_item):
        return self.bounding_rectangle.contains(work_item.bounding_rectangle)

    def __repr__(self):
        return f"WorkflowStep(bounding_rectangle={self.bounding_rectangle})"

    def associate_with(self, work_items: WorkItems) -> None:
        for work_item in work_items:
            if self.contains(work_item):
                self.number_of_work_items += 1
