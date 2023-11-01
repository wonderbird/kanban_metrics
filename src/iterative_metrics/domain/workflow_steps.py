from typing import Iterator, List, Any

import cv2
import numpy as np

from iterative_metrics.adapters.outbound.find_bounding_rectangles_of_largest_closed_shapes import (
    find_bounding_rectangles_of_largest_closed_shapes,
)
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_step import WorkflowStep


class WorkflowSteps:
    def __init__(self, workflow_steps: List[WorkflowStep]) -> None:
        self.workflow_steps = workflow_steps

    def __iter__(self) -> Iterator[WorkflowStep]:
        return iter(self.workflow_steps)

    def __getitem__(self, index: Any) -> Any:
        return self.workflow_steps[index]

    @property
    def count(self) -> int:
        return len(self.workflow_steps)

    @property
    def work_items_per_workflow_step(self) -> List[int]:
        result = [
            workflow_step.number_of_work_items for workflow_step in self.workflow_steps
        ]
        return result

    @staticmethod
    def parse_screenshot(screenshot: np.ndarray) -> "WorkflowSteps":
        hsv_input = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

        # find the workflow step boxes
        lower_boundary = np.array([0, 0, 200])
        upper_boundary = np.array([0, 0, 255])
        boxes_with_text = cv2.inRange(hsv_input, lower_boundary, upper_boundary)

        # remove the text and other small artifacts
        kernel = np.ones((3, 3), np.uint8)
        boxes = cv2.erode(boxes_with_text, kernel, iterations=2)
        boxes = cv2.dilate(boxes, kernel, iterations=2)
        bounding_rectangles = find_bounding_rectangles_of_largest_closed_shapes(boxes)

        # for overlapping bounding rectangles, only keep the larger one
        sorted_rectangles = sorted(
            bounding_rectangles, key=lambda rect: rect.area, reverse=True
        )
        largest_rectangles = []
        for rectangle in sorted_rectangles:
            if not any(
                [
                    rectangle.intersects(large_rectangle)
                    for large_rectangle in largest_rectangles
                ]
            ):
                largest_rectangles.append(rectangle)

        # sort rectangles from left to right
        largest_rectangles = sorted(largest_rectangles, key=lambda rect: rect.x)

        # convert rectangles to workflow steps
        workflow_steps = []
        for rectangle in largest_rectangles:
            workflow_steps.append(WorkflowStep(rectangle))

        return WorkflowSteps(workflow_steps)

    def associate_with(self, work_items: WorkItems) -> None:
        """Map each work item to the workflow step it belongs to."""
        for workflow_step in self.workflow_steps:
            workflow_step.associate_with(work_items)

    def remove_areas_smaller_than_a_work_item(self, work_items: WorkItems) -> None:
        if work_items.count == 0:
            return

        smallest_rectangle = work_items[0].bounding_rectangle
        item_indices_to_keep = []
        for index, workflow_step in enumerate(self.workflow_steps):
            if (
                workflow_step.bounding_rectangle.height > smallest_rectangle.height
                and workflow_step.bounding_rectangle.width > smallest_rectangle.width
            ):
                item_indices_to_keep.append(index)

        self.workflow_steps = [
            self.workflow_steps[index] for index in item_indices_to_keep
        ]
