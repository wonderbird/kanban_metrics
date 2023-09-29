import numpy as np

from iterative_metrics.adapters.outbound.find_workflow_steps_in_image import (
    find_workflow_steps_in_screenshot,
)


class WorkflowSteps:
    def __init__(self, workflow_steps):
        self.workflow_steps = workflow_steps

    @property
    def count(self) -> int:
        return len(self.workflow_steps)

    @staticmethod
    def parse_screenshot(screenshot: np.ndarray) -> "WorkflowSteps":
        workflow_steps = find_workflow_steps_in_screenshot(screenshot)
        return WorkflowSteps(workflow_steps)
