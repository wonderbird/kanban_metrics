from typing import Iterator

import numpy as np

from iterative_metrics.adapters.outbound.find_workflow_steps_in_image import (
    find_workflow_steps_in_screenshot,
)
from iterative_metrics.domain.workflow_step import WorkflowStep


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

    def __iter__(self) -> Iterator[WorkflowStep]:
        return iter(self.workflow_steps)
