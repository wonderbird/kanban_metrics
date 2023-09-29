from iterative_metrics.domain.work_items import WorkItems


class WorkflowStep:
    def __init__(self, bounding_rectangle):
        self.bounding_rectangle = bounding_rectangle
        self.work_items = WorkItems([])

    def contains(self, work_item):
        return self.bounding_rectangle.contains(work_item.bounding_rectangle)

    @property
    def number_of_work_items(self) -> int:
        return self.work_items.count

    def __repr__(self):
        return f"WorkflowStep(bounding_rectangle={self.bounding_rectangle})"
