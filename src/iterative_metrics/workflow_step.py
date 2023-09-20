class WorkflowStep:
    def __init__(self, bounding_rectangle):
        self.bounding_rectangle = bounding_rectangle

    def __repr__(self):
        return f"WorkflowStep(bounding_rectangle={self.bounding_rectangle})"
