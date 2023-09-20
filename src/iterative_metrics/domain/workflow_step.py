class WorkflowStep:
    def __init__(self, bounding_rectangle):
        self.bounding_rectangle = bounding_rectangle

    def contains(self, work_item):
        return self.bounding_rectangle.contains(work_item.bounding_rectangle)

    def __repr__(self):
        return f"WorkflowStep(bounding_rectangle={self.bounding_rectangle})"
